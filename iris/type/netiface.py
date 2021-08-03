import netifaces


class NetworkInterface(str):
    """ Network interface type string object """

    def __init__(self, iface):
        if not str(iface) in netifaces.interfaces():
            raise ValueError('Invalid network interface')
