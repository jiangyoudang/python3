import socket

PORT = 50039
MAX = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('127.0.0.1',PORT))

# client.sendto(b'msgsffsefs',('127.0.0.1',PORT))
client.connect(('127.0.0.1',PORT))
client.send(b'hello world')
data, addr = server.recvfrom(MAX)

string = 'data:{} is at {}'.format(data,addr)
print(string)
# client.connect(('127.0.0.1',PORT))
# client.send('hello')

# print(conn.recv(1024))
# print(server.getsockname())
print(client.getsockname())
# print(server.recv(1024))