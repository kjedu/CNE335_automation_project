from http.client import responses
import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response =  os.system(f"ping -c 5 {self.server_ip}") # -c 5 for macOS instead of -n 5
        if response == 0:
            return f"{self.server_ip} ping was successful" # at least one reply was received, good
        else:
            return f"{self.server_ip} ping was not successful" # no replies were received, 100% lost, bad