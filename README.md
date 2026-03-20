# diii

A basic REPL for [iii](https://monome.org/docs/iii/) devices

A fork of [druid](https://github.com/monome/druid) (which is for [crow](https://github.com/monome/crow))


## Setup

`diii` requires Python v3.13

Install [uv](https://docs.astral.sh/uv/#installation), a Python project manager.

Using the command line, navigate to the folder where you want to install `diii`:

```
mkdir ~/diii
cd ~/diii
uv venv --python 3.13
source .venv/bin/activate
uv pip install monome-diii
```

And then to run diii

```
diii
```

## diii

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

