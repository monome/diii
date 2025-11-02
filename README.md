# diii

A basic REPL for [iii](https://monome.org/docs/iii/) devices

A fork of [druid](https://github.com/monome/druid) (which is for [crow](https://github.com/monome/crow))

## v1.1.0 beta

To get the pre-release beta:

```
pip3 install monome-diii --pre
```

To see your current version:

```
diii --version
```

## Setup

Requirements:
- Python 3.6+
  - Windows & OS X: https://www.python.org/downloads/
  - Linux: `sudo apt-get install python3 python3-pip` or equivalent
- `pip` and `setuptools`
- `pyserial` and `prompt_toolkit`

Note: you might need to use `python` and `pip` instead of `python3` and `pip3` depending on your platform. If `python3` is not found, check that you have python >= 3.6 with `python --version`.

Install:
```bash
pip3 install monome-diii

Run:
```
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

Sometimes you don't need the repl, but just want to upload/download scripts to/from device. You can do so directly from the command line with the `list`, `upload` and `download` commands.

### List

```
diii list
```

Lists files currently on device.

### Upload

```
diii upload script.lua
```

Uploads the provided lua file `script.lua` to device and stores it in flash.

### Download

```
diii download script.lua
```

Prints the file `script.lua` which is on the device, if it exists. If you'd like to save the file to the local disk, do this:

```
diii download script.lua > script.lua
```

