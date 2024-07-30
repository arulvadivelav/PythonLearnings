import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 8000

# Bind IP address with Port
server_socket.bind((IP, PORT))

"""Provide maximum connectins to connect"""
server_socket.listen(4)

while True:
    client, client_address = server_socket.accept()
    print(client,client_address)
    False
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # server_socket.bind(('localhost', 80))  # Use 0 to bind to any available port

# # Get the IP address and port number
# # ip_address, port = server_socket.getsockname()
# # print(ip_address, port)

# server_socket.bind((IP, PORT))

# ip_address, port = server_socket.getsockname()
# print(ip_address, port)