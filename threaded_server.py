import socket
import threading

clients = []
clients_lock = threading.Lock()

def handle_client(client_socket, address):
	print(f"[+] New thread started for {address}")
	with clients_lock:
		clients.append(address)
	with client_socket:
		while True:
			data = client_socket.recv(1024)
			if not data:
				print(f"[-] {address} is disconnected")
				break

			for client in clients:
				client.send((f"{address}: {data.decode()}").encode())
			print(f"[{address}] {response}")

if __name__ == "__main__":
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('127.0.0.1', 5050))
	server_socket.listen(5)
	print("[*] Server started")
	
	try:
		while True:
			client_socket, address = server_socket.accept()
			client_thread = threading.Thread(
				target=handle_client,
				args=(client_socket, address)
			)
			client_thread.daemon = True
			client_thread.start()
	
	except KeyboardInterrupt:
		print("\n[*] Server closed")
		server_socket.close()
