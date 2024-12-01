## Setup
First create a [virtual environment](https://docs.python.org/3/library/venv.html) and then do an [editable install](https://pip.pypa.io/en/latest/reference/pip_install/#editable-installs) of diii.
```
cd <directory where repository is checked out>
# Create virtual environment
python3 -m venv .venv

# Active the virtual environment
# Linux / Mac OS
source .venv/bin/activate
# Windows
source .venv/Scripts/activate

# Do an editable install
pip install -e .
# Activate the virtual environment again to update virtual environment $PATH
source .venv/bin/activate

# Now execute diii, which runs directly from the code from this directory
# Linux / Mac OS / Windows(PowerShell)
diii
# Windows (GIT Bash)
winpty diii
```

Closing the terminal will also exit the virtual environment. Running `deactivate` will exit the virtual environment as well.

If at a later point you want to start working again it's enough to activate the virtual environment again using
```
cd <directory of repository)
source .venv/bin/activate
diii
```

## Package Update

- pypi.org account, get token for __token__ entry

```
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```
