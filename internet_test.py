import socket
import time

import logging
logger = logging.getLogger(__name__)

def isConnected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False



if __name__ == "__main__":
    for x in range(5):
        print(isConnected())
        time.sleep(2)
