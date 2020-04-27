import tkinter as tk
import os
    

def write_slogan():
    os.system("gnome-terminal -e 'bash -c \"python3 qr-filetransfer-universal.py -f check_pic.jpeg; exec bash\"'")

def client():
    os.system("gnome-terminal -e 'bash -c \"python2 client.py; exec bash\"'")

def bot():
    os.system("gnome-terminal -e 'bash -c \"python3 chatbot/chatbot.py; exec bash\"'")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Transfer_files_from_pc_to_mobile",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)
client_open = tk.Button(frame,
                   text="open_client",
                   command=client)
client_open.pack(side=tk.LEFT)

bot_open = tk.Button(frame,
                   text="open_bot",
                   command=bot)
bot_open.pack(side=tk.LEFT)



root.mainloop()
