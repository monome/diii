# diii

A basic REPL for iii devices

A fork of [druid](https://github.com/monome/druid) (which is for [crow](https://github.com/monome/crow))

## Setup

Requirements:
- Python 3.6+
  - Windows & OS X: https://www.python.org/downloads/
  - Linux: `sudo apt-get install python3 python3-pip` or equivalent
- `pip` and `setuptools`
- `pyserial` and `prompt_toolkit`

Note: you might need to use `python` and `pip` instead of `python3` and `pip3` depending on your platform. If `python3` is not found, check that you have python >= 3.6 with `python --version`.

Install and run:
```bash
# Install diii
pip3 install monome-diii
# Run diii :)
diii
```

## diii

Start by running `diii`

- type q (enter) to quit.
- type h (enter) for a list of special commands.

- will reconnect to device after a disconnect / restart
- scrollable console history

Example:

```
  q to quit. h for help

> x=6

> print(x)
6

> q
```

Diagnostic logs are written to `diii.log`.

## Command Line Interface

Sometimes you don't need the repl, but just want to upload/download scripts to/from device. You can do so directly from the command line with the `upload` and `download` commands.

### Upload

```
diii upload script.lua
```

Uploads the provided lua file `script.lua` to device and stores it in flash to be executed on boot.

### Download

```
diii download > feathers.lua
```

Grabs the script currently stored on device, and pastes the result into a new file `feathers.lua`.

