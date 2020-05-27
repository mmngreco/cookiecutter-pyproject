# Python Project Template

## Offers

* `.gitignore`
* versioneer
* `setup.py`
* `src/pkg` skeleton
* Sphinx
* pytest
* tox
* flake8
* `pyproject.toml`
* `CHANGELOG.md`
* `README.md`

## Quickstart

```bash
pip install cookiecutter
cookiecutter gh:mmngreco/cookiecutter-pyproject
```

other way (without prompt):

```
cookiecutter --no-input \
    gh:mmngreco/cookiecutter-pyproject \
    year=2020 \
    project_author=mmngreco \
    project_name=my_lib \
    project_src=my_lib \
    project_url=https://github.com/mmngreco/my_lib \

```
