import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5050))

server_socket.listen(5)
print('Server is Started')

while True:
	client_socket, address = server_socket.accept()
	print(rf'Connection from {address}')
	data = client_socket.recv(1024)
	if data:
		buf = ("Echo: " + data.decode())
		client_socket.send(buf.encode())
		print(rf'Sent back: {buf}')
	client_socket.close()
