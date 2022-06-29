# WIP ghpages

## Upload 手順

1. tmp のパスを作成
1. tmp にリポジトリ@gh-pagesをclone
1. clone したリポジトリのファイルを全消し git rm -rf .
1. clone したリポジトリに dist(アップロードしたい対象)内のファイルをコピーする
1. clone したリポジトリで add .
1. clone したリポジトリで commit
1. clone したリポジトリで push --force
1. tmp さよなら

Thanks: https://github.com/tschaub/gh-pages

## Development

setup
```console
poetry install
```

activate
```console
poetry shell
```

setup pre-commit
```console
poetry run pre-commit install
```

run tox
```console
poetry run tox
```
