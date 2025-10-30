import asyncio
import logging
import time
import os

import serial
import serial.tools.list_ports

from diii.exceptions import DeviceNotFoundError


logger = logging.getLogger(__name__)

def find_serial_port(hwid):
    for portinfo in serial.tools.list_ports.comports():
        if hwid in portinfo.hwid: # must match VID:PID
            if os.name == "nt": # windows doesn't know the name of the device
                return portinfo
            if "iii" in portinfo.product: # more precise detection for linux/macos
                return portinfo
    raise DeviceNotFoundError(f"can't find iii device")

class Deviceiii:
    def __init__(self, serial=None):
        self.serial = None
        self.is_connected = False
        self.event_handlers = {}

    def find_device(self):
        portinfo = find_serial_port('USB VID:PID=CAFE:1101')
        try:
            return serial.Serial(
                portinfo.device,
                baudrate=115200,
                timeout=0.1,
            )
        except serial.SerialException as e:
            raise DeviceNotFoundError("can't open serial port", e)

    def __enter__(self):
        return self

    def __exit__(self, exc, exc_type, traceback):
        if self.is_connected:
            self.disconnect()

    def connect(self):
        self.serial = self.find_device()
        logger.info(f'connected to device on {self.serial.port}')

    def disconnect(self):
        if self.serial is not None:
            self.serial.close()

    def raise_event(self, event, *args, **kwargs):
        try:
            handlers = self.event_handlers[event]
        except KeyError:
            pass
        else:
            for handler in handlers:
                try:
                    handler(*args, **kwargs)
                except Exception as exc:
                    logger.error(f'error in command handler "{event}" ({handler}): {exc}')

    def replace_handlers(self, handlers):
        self.event_handlers = handlers

    def reconnect(self, err_event=False):
        try:
            self.connect()
            self.is_connected = True
            self.raise_event('connect')
        except Exception as exc:
            if self.is_connected or err_event:
                self.is_connected = False
                self.raise_event('connect_err', exc)

    def writebin(self, b):
        if len(b) % 64 == 0:
            b += b'\n'
        logger.debug(f'-> {b}')
        self.serial.write(b)

    def write(self, s):
        self.writebin(s.encode('utf-8'))

    def writeline(self, line):
        self.write(line + '\n')

    def writefile(self, fname):
        with open(fname) as f:
            logger.info(f'opened file: {f}')
            for line in f.readlines():
                self.writeline(line.rstrip())
                time.sleep(0.001)


    def upload(self, fname):
        self.raise_event('uploading', fname)
        self.writeline('^^s')
        time.sleep(0.1)
        self.writeline(os.path.basename(fname))
        time.sleep(0.1)
        self.writeline('^^f')
        time.sleep(0.1)
        self.writeline('^^s')
        time.sleep(0.1)
        self.writefile(fname)
        time.sleep(0.1)
        self.writeline('^^w')
        time.sleep(0.1)

    def readbin(self, count):
        b = self.serial.read(count)
        if len(b) > 0:
            logger.debug(f'<- {b}')
        return b

    def read(self, count):
        return self.readbin(count).decode('utf-8')

    async def read_forever(self):
        while True:
            sleeptime = 0.001
            try:
                r = self.read(10000)
                if len(r) > 0:
                    lines = r.split('\n')
                    for line in lines:
                        self.process_line(line)
            except Exception as exc:
                if self.is_connected:
                    logger.error(f'lost connection: {exc}')
                sleeptime = 0.1
                self.reconnect()
            await asyncio.sleep(sleeptime)

    def process_line(self, line):
        if "^^" in line:
            cmds = line.split('^^')
            for cmd in cmds:
                t3 = cmd.rstrip().partition('(')
                if not any(t3):
                    continue
                evt = t3[0]
                args = t3[2].rstrip(')').split(',')
                self.raise_event('iii_event', line, evt, args)
        elif len(line) > 0:
            self.raise_event('iii_output', line)
