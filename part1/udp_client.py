'''
Varun Ved
Justin Mendiguarin

udp_client.py

Client part of the code for server-client
'''

import socket
import sys

HOST = '127.0.0.1'
PORT = 7777

'''
socket_init()
creates a new instance of socket
'''
def socket_init():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return c

'''
sends a message to the socket
@param string message
@param socket c
'''
def socket_send(message, c):
    c.sendto(message, (HOST, PORT))

'''
recieves a message to the socket
@param socket c
'''
def socket_recieve(c):
    upperMessage, address = c.recvfrom(2048)
    print('Server Response: ', upperMessage)

'''
closes the socket
@param socket c
'''
def socket_close(c):
    c.close()
    sys.exit('Closing Client')

'''
main running file, expects socket
@param socket c
'''
def run(c):
    message = raw_input('Enter the message you want to send ')
    if message == 'exit':
        socket_send(message, c)
        socket_close(c)
    else:
        socket_send(message, c)
        socket_recieve(c)
'''
main driver
'''
if __name__ == "__main__":
    sock = socket_init()
    while True:
        run(sock)
