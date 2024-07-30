import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 8000

server.connect((IP,PORT))


