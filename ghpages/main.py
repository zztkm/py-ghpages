import argparse
import os
import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from commando import Commando

from . import __version__

cmd = Commando()


def copy_all(src: Path, dst: Path):
    for path in src.iterdir():
        if path.is_dir():
            dir_path = dst / path.name
            shutil.copytree(path.resolve(), dir_path)
        else:
            shutil.copy2(str(path.resolve()), str(dst))


def publish(dst: str):
    output_dir = Path(dst).resolve()
    deployment_branch = "gh-pages"
    res = cmd.run("git config --get remote.origin.url")
    repo_url = res.stdout.decode(sys.getfilesystemencoding()).strip()

    with TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)  # カレントディレクトリを　tmpdirに移動

        clone_cmd = ["git", "clone", "--depth", "1", "--branch", deployment_branch, repo_url, tmpdir]
        res = cmd.run(clone_cmd)

        if res.returncode == 0:
            cmd.run("git rm -rf .")
        else:
            cmd.run("git init")
            cmd.run(f"git checkout -b {deployment_branch}")
            cmd.run(f"git remote add origin {repo_url}")

        copy_all(output_dir, Path(tmpdir))

        cmd.run("git add --all")
        cmd.run('git commit -m "update"')

        print(os.getcwd())
        res = cmd.run(f"git push --force origin {deployment_branch}")
        if res.returncode == 0:
            print("Successful push gh-pages")
        else:
            print(res.args)
            print(res.stderr.decode(sys.getfilesystemencoding()))
            sys.exit(res.returncode)


def main():
    parser = argparse.ArgumentParser(description="Publish files to a gh-pages branch on GitHub")

    parser.add_argument("-v", "--version", action="version", version=f"ghpages version: {__version__}")
    parser.add_argument("dist", help="Source directory of the page you want to publish")

    args = parser.parse_args()

    publish(args.dist)
