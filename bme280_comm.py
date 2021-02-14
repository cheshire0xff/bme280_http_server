import socket

class Bme280Device:
    def __init__(self, udp_address, upd_port = 3333):
        self.udp_tx_info = (udp_address, upd_port)
        self.sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM)

    def send_command(self, cmd):
        cmd_bytes = cmd.encode('utf-8')
        self.sock.sendto(cmd_bytes, 
                self.udp_tx_info)
        data, addr = self.sock.recvfrom(1024)
        return data.decode('utf-8')
