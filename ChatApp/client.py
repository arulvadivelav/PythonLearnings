import socket
from tkinter import *


def send(listbox, entry):
    # Send a message to the server
    message = entry.get()
    listbox.insert("end", "Me: "+message)
    client_socket.send(bytes(message, "utf-8"))


def receive(listbox):
    # Receive a message from the client and set 100 for the length of the input
    message_from_client = client_socket.recv(100)
    listbox.insert("end", "Server: " + message_from_client.decode("utf-8"))


# Set tkinter to show the messages
root = Tk()
root.title("Reciver")

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

send_button = Button(root, text="Send", command=lambda: send(listbox, entry))
send_button.pack(side=BOTTOM)

receive_button = Button(root, text="Receive", command=lambda: receive(listbox))
receive_button.pack(side=BOTTOM)

# Socket connection to send and receive messages
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 8000

# Bind IP address with Port
client_socket.connect((IP, PORT))

# Run a Tkinter
root.mainloop()
