
# Echo server program
import socket
import sys

HOST = '127.0.0.100'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
conn = None
addr = None


def getting_message():
    """
    used to get the message from the robot
    :return data: return the message that we get from the robot
    """

    global s,conn,addr
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                                  socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.bind(sa)
            s.listen(1)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
        # conn.send(data)

    return data


def resenting_message(message):
    """
    used to send message back to the robot

    :param message: string, specific sentence of particular scenario
    :return:
    """
    conn.send(message.encode('utf-8'))
        # here we must send byte type
