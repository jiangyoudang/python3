
import socket
import time

#create socket
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

host = socket.gethostname()

port = 9999

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()

    print('get message from {}'.format(addr))

    current_time = time.ctime(time.time())

    client_socket.send(current_time.encode('ascii'))

    client_socket.close()


