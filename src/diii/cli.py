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

@cli.command(short_help="Download a file from device")
def download():
    """
    Download a file from device and print it to screen
    """
    with Deviceiii() as iii:
        iii.connect()
        iii.writeline('^^p')
        time.sleep(0.3)
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
        time.sleep(0.3)
        iii.upload(filename)
        #time.sleep(0.3)
        click.echo(iii.read(1000000))
        #time.sleep(1.0)
        #iii.writeline('^^p')
        #time.sleep(0.3)
        #click.echo(iii.read(1000000))

@cli.command(short_help="Read flash index from device")
@click.argument("index", type=click.INT, required=True)
def flash_read(index):
    """
    Download a flash index from device and print it to screen
    INDEX is the flash index
    """
    with Deviceiii() as iii:
        iii.connect()
        cmd = 'print(flash_read('+str(index)+'))\n'
        iii.writeline(cmd)
        time.sleep(0.3)
        click.echo(iii.read(1000000))

@cli.command(short_help="Write file to flash index on device")
@click.argument("index", type=click.INT, required=True)
@click.argument("filename", type=click.Path(exists=True))
def flash_write(index,filename):
    """
    Write file to flash index on device.
    INDEX is the flash index
    FILENAME is the path to the file to upload
    """
    with Deviceiii() as iii:
        iii.connect()
        time.sleep(0.3)
        file = open(filename).read().replace('\n','')
        send = "flash_write("+str(index)+",'"+file+"')\n"
        click.echo(send)
        #iii.upload(filename)
        iii.writeline(send)
        #time.sleep(0.3)
        click.echo(iii.read(1000000))
        #time.sleep(1.0)
        #iii.writeline('^^p')
        #time.sleep(0.3)
        #click.echo(iii.read(1000000))

@cli.command()
@click.argument("filename", type=click.Path(exists=True), required=False)
@click.option("--theme/--no-theme", default=True, show_default=True,
              help="Whether to use the internal color theme.")
def repl(filename, theme):
    """ Start interactive terminal """
    diii_repl.main(filename, theme)
