# Repo for Testing Django Packages


## Prerequisites

- **_[python](https://www.python.org/downloads/) 3.12_** : It will be constantly updated. So, If you are familiar with Python setup, recommend to use [pyenv](https://github.com/pyenv/pyenv) which is python version management package. There is [window version of pyenv](https://github.com/pyenv-win/pyenv-win) too.
- **_[pip](https://pip.pypa.io/en/stable/installation/) or [pipX](https://pypa.github.io/pipx/installation/)_** : Recommend to use just one of them to install packages. I personally prefer to use pipx because of easier commands.

## Quickstart

Make sure you added your ssh key to your github account. If you don't know what it is follow [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

If you already added your ssh key, run the following command on your terminal to clone the repo.

```shell
git clone git@github.com:jisoooh0202/test_django.git
```

\*\*\* Never use the master branch unless you are the admin.

```shell
cd test_django
```

Run the following command on your terminal to create the Virtual Environment.
```shell
python -m venv venv
```

Activate the venv with following commands
```shell
source venv/bin/activate ## Linux
venv\Scripts\activate ## Windows
```

Install the packages
```shell
python -m pip install -r requirements.txt
```

Run server
```shell
python manage.py runserver
```