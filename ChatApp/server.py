import socket
from tkinter import *


def send(listbox, entry):
    # Send a message to the client
    message = entry.get()
    listbox.insert("end", "Me: "+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))


def receive(listbox):
    # Receive a message from the client and set 100 for the length of the input
    message_from_client = client.recv(100)
    listbox.insert("end", "Client: " + message_from_client.decode("utf-8"))


# Set tkinter to show the messages
root = Tk()
root.title("Server")
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

send_button = Button(root, text="Send", command=lambda: send(listbox, entry))
send_button.pack(side=BOTTOM)

receive_button = Button(root, text="Receive", command=lambda: receive(listbox))
receive_button.pack(side=BOTTOM)

# Socket connection to send and receive messages
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 8000

# Bind IP address with Port
server_socket.bind((IP, PORT))

# Provide maximum connectins to connect
server_socket.listen(4)

client, client_address = server_socket.accept()

# Run a Tkinter
root.mainloop()
