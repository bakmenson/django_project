from sys import argv, exit
from pyenv import get_command_output, install_python, create_virtualenv, \
    set_virtualenv


def print_message(message: str) -> None:
    print(f"{'-' * len(message)}\n{message}\n{'-' * len(message)}")


def print_help() -> None:
    print('-' * 70)
    print('''
  First arg:
    -h: print help
    -c: create django project
    -d: delete django project

  Second arg:
    project directory to be created

  Third arg:
    virtual env to be created or set for project

  Fourth arg:
    python version (e.g. 3.8.0) to be installed or set for project
          ''')
    print('-' * 70)


def set_project_arg(input_descr: str, is_empty: bool = False) -> str:
    project_arg: str = input(input_descr + ": >>> ")

    if not is_empty:
        while True:
            if not project_arg:
                print("Missed project variable. Try again.")
                project_arg = input(input_descr + ": >>> ")
                continue
            break

    return project_arg


# TODO add .vim/coc-setting.json for pyenv and coc.nvim
# using commands: pyenv which python
# and write output like /home/solus/.pyenv/versions/django-ecommerce/bin/python
# in .vim/coc-setting.json

project_action: str = str()

try:
    project_action = argv[1]
except IndexError:
    print_message("Missed project argument.")
    exit()

if project_action == "-h":
    print_help()
    exit()

project_dir: str = set_project_arg("Input project dir name")
virtual_env: str = set_project_arg("Input virtual evn name")
python_version: str = set_project_arg("Input python version (e.g. 3.8.0)",
                                      True)

VIRTUALENV_PATTERN = r"^([a-zA-Z0-9.-]+)..created.+versions.(.+).$"
VERSION_PATTERN = r"^[a-zA-Z0-9.-]+$|^[a-zA-Z0-9.-]+\s"

if project_action == '-c':

    versions = get_command_output("pyenv versions", VERSION_PATTERN)
    virtualenvs = get_command_output("pyenv virtualenvs", VIRTUALENV_PATTERN)

    print(versions)
    print(virtualenvs)

elif project_action == '-d':
    pass
else:
    if project_action:
        print_help()
