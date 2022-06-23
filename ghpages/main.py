import argparse

from . import __version__


def main():
    parser = argparse.ArgumentParser(description="Publish files to a gh-pages branch on GitHub")

    parser.add_argument("-v", "--version", action="version", version=f"ghpages version: {__version__}")