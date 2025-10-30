""" Command-line interface for diii """

import sys
import time

import click

import requests
import os
from packaging import version

from diii import __version__
from diii.iii import Deviceiii
from diii import repl as diii_repl

@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(__version__)
def cli(ctx):
    """ Terminal interface for iii devices """
    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)

@cli.command(short_help="List files on device")
def list():
    """
    List files on device
    """
    with Deviceiii() as iii:
        iii.connect()
        iii.writeline('for _,x in pairs(fs_list_files()) do print(x) end')
        time.sleep(0.3)
        click.echo(iii.read(1000000))

@cli.command(short_help="Download a file from device")
@click.argument("filename")
def download(filename):
    """
    Download a file from device and print it to screen
    """
    with Deviceiii() as iii:
        iii.connect()
        time.sleep(0.1)
        iii.writeline('^^s')
        click.echo(iii.read(1000000))
        time.sleep(0.1)
        iii.writeline(filename)
        time.sleep(0.1)
        iii.writeline('^^f')
        click.echo(iii.read(1000000))
        time.sleep(0.1)
        click.echo(iii.read(1000000))
        iii.writeline('^^p')
        time.sleep(0.1)
        click.echo(iii.read(1000000))

@cli.command(short_help="Upload a file to device")
@click.argument("filename", type=click.Path(exists=True))
def upload(filename):
    """
    Upload a file to device.
    FILENAME is the path to the lua file to upload
    """
    with Deviceiii() as iii:
        iii.connect()
        iii.writeline('^^s')
        click.echo(iii.read(1000000))
        time.sleep(0.1)
        iii.writeline(os.path.basename(filename))
        time.sleep(0.1)
        iii.writeline('^^f')
        click.echo(iii.read(1000000))
        time.sleep(0.1)
        #iii.writeline('^^g')
        #click.echo(iii.read(1000000))
        #time.sleep(0.1)
        iii.upload(filename)
        time.sleep(0.1)
        click.echo(iii.read(1000000))

@cli.command()
@click.argument("filename", type=click.Path(exists=True), required=False)
@click.option("--theme/--no-theme", default=True, show_default=True,
              help="Whether to use the internal color theme.")
def repl(filename, theme):
    """ Start interactive terminal """
    diii_repl.main(filename, theme)
