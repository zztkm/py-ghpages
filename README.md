# ghpages

ghpages is a CLI tool for easily publishing static content to GitHub Pages.

For example, it is useful to publish API documentation generated by [Sphinx](https://www.sphinx-doc.org/en/master/)

## Install

```
pip install ghpages
```

## Usage

Publish the contents of the `dist` directory
```shell
ghpages dist
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

