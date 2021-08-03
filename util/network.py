import socket


class NetworkUtil:

    @staticmethod
    def is_tcp_port_open(address: str, port: int, timeout: int = 2500) -> bool:
        """ Check if TCP port is open on specified address """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout / 1000)

        try:
            s.connect((address, port))
            s.close()

            return True
        except Exception:
            return False
