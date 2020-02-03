import sys

from Payload import Payload
from socket import socket


class Payload_Kernel(Payload):
    exploits = []

    def __init__(self, exploits):
        super().__init__()
        self.exploits = exploits

    def local_command(self):
        for e in self.exploits:
            sys.popen("cp " + e + " .")

    def remote_command(self, remote_socket: socket):
        # wget stuff
        # send script.py
        # run script.py
        pass
