'''
server.py

The server for our chat
Varun Ved
Justin Mendiguarin
'''
import sys
import socket
import select

HOST = ''
SOCKETS = []
RECV_BUFFER = 4096
PORT = 9009

'''
start_chat
execution of the chat program
'''
def start_chat():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(10)

    # a list of connections
    SOCKETS.append(s)

    print "Chat server started on port " + str(PORT)

    while True:

        ready_to_read,ready_to_write,in_error = select.select(SOCKETS,[],[],0)

        for sock in ready_to_read:
            # a new connection request recieved
            if sock == s:
                sockfd, addr = s.accept()
                SOCKETS.append(sockfd)
                print "A client (%s, %s) has joined!" % addr

                broadcast(s, sockfd, "%s:%s entered our chatting room\n" % addr)

            # a message from a client, not a new connection
            else:
                # data recieved
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data != 'exit':
                        broadcast(s, sock, "\r" + str(sock.getpeername()) + ' ' + data)
                    elif str(data) == 'exit':
                        sys.exit('EXIT TYPED, QUITTING')
                    else:
                        # empty response
                        if sock in SOCKETS:
                            SOCKETS.remove(sock)
                        broadcast(s, sock, "Client (%s, %s) has exited\n" % addr)

                except:
                    broadcast(s, sock, "Client (%s, %s) has exited\n" % addr)
                    continue

    s.close()

'''
broadcast
@param socket s
@param socket sock
@param string message
'''
def broadcast (s, sock, message):
    for socket in SOCKETS:
        # send the message only to one peer
        if socket != s and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                if socket in SOCKETS:
                    SOCKETS.remove(socket)

if __name__ == "__main__":
    sys.exit(start_chat())
