import socket
import ipaddress as ip

class Bme280Device:
    def __init__(self, udp_address, upd_port = 3333):
        self.udp_tx_info = (str(udp_address), upd_port)
        if isinstance(udp_address, ip.IPv6Address):
            socket_type = socket.AF_INET6
        else:
            socket_type = socket.AF_INET
        self.sock = socket.socket(
                socket_type,
                socket.SOCK_DGRAM)

    def send_command(self, cmd):
        cmd_bytes = cmd.encode('utf-8')
        self.sock.sendto(cmd_bytes, 
                self.udp_tx_info)
        data, addr = self.sock.recvfrom(1024)
        return data.decode('utf-8')
