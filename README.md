# ghpages

ghpages is a CLI tool for easily publishing static content to GitHub Pages.

## Install

```
pip install ghpages
```

## Usage

Publish the contents of the `dist` directory
```shell
gh-pages dist
```

Congratulations! If you see a success message, you are ready to publish on GitHub Pages!

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

