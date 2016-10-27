'''
Varun Ved
Justin Mendiguarin

udp_server.py

Server part of simple client server chat
'''

import socket
import sys

HOST = '127.0.0.1'
PORT = 6969

'''
socket_init()
creates socket
@returns socket.host
'''
def socket_init():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST,PORT))
    print 'Server is ready'
    return s

'''
socket_parse()
parses input and sends connection reply
@param socket conn
'''
def socket_parse(conn):
    message, addr = s.recvfrom(2048)
    capitalMessage = message.upper()
    if capitalMessage == 'EXIT' or capitalMessage == 'exit':
        conn.close()
        sys.exit('Connection closed, program exiting')
        return False
    else:
        socket_send(conn, capitalMessage)
        return True

'''
socket_send
sends the message to the connection
@param socket conn
@param string message
'''
def socket_send(conn, capitalMessage):
    conn.sendto(capitalMessage, (HOST, PORT))

if __name__ == "__main__":
    conn = socket_init()
    while(socket_parse(conn) == True):
        pass
    sys.exit(0)
