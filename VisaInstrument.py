import pyvisa as visa
from datetime import datetime
import signal


class VISAInstrument(object):

    def __init__(self, resourceID: str, timeout: int = 1000, showIDN: bool = True, reset: bool = False):
        '''
        Init visa instrument
        resourceID: your instrument id.
                    If you do not know this para of your instrument, 
                    you can run VisaInstrument.list_devices() to show 
                    all VISA device IDs.

        timeout:    instrument timeout in ms
                    /default 1000ms/

        show IDN:   whether show your instrument info 
                    /default True/
                    If your device do not support *IDN? command,
                    you can set this para False.

        reset:      whether reset your instrument after connection
                    /default False/
                    If your device do not support *RST command,
                    you should override reset() method to make this
                    option work.
        '''

        self.resourceID = resourceID

        # Connect Visa device
        try:
            self.resource = visa.ResourceManager().open_resource(resourceID)
            self.resource.timeout = timeout
            signal.signal(signal.SIGINT, lambda signal, frame: self.resource.close())
        except BaseException as e:
            print(datetime.now(), 'Error in open device at: {}'.format(resourceID), e)

        # Instrument information
        if showIDN:
            print(datetime.now(), self.query("*IDN?").strip().replace(",", " "), "connected.")

        # Reset
        if reset:
            self.reset()

    def __del__(self):
        if self.resource:
            self.resource.close()

    def reset(self):
        self.resource.write("*RST")
        print(datetime.now(), "resource reset")

    def write(self, command: str):
        return self.resource.write(command)

    def query(self, command: str):
        return self.resource.query(command)

    def command(self, command: str):
        if command.endswith("?"):
            return self.query(command)
        else:
            return self.write(command)

    def print_info(self):
        info = self.query("*IDN?")
        print(datetime.now(), info)

    @staticmethod
    def list_devices():
        devices = visa.ResourceManager().list_resources()
        print("VISA Devices:")
        for device in devices:
            print(device)
