import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 8000

server.connect((IP,PORT))


# import tkinter as tk

# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()