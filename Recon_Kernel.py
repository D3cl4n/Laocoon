from socket import socket

from Recon import Recon


class Recon_Kernel(Recon):

    def __init__(self):
        super().__init__()

    def get_info(self, remote_socket: socket):
        pass
        # What we have
        # get_kernel_version
        # return info

    def parse(self, info):
        # parse_kernel_version
        # exploit_lookup
        # return payload
        pass
