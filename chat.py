import threading
import tkinter as tk
from tkinter import scrolledtext
from client import Client


class ChatGUI:
    def __init__(self, server_host, server_port, client_name):
        self.server_host = server_host
        self.server_port = server_port
        self.client_name = client_name

        self.client = Client(self.server_host, self.server_port, self.client_name)
        self.root = tk.Tk()
        self.root.title("Chat")

        # Text widget to display messages
        self.message_display = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.message_display.configure(state='disabled')
        self.message_display.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Entry widget to type message
        self.message_entry = tk.Entry(self.root, width=80)
        self.message_entry.pack(side=tk.LEFT, padx=5, pady=5)

        # Button to send message
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Start receiving messages in a separate thread
        receive_thread = threading.Thread(target=self.client.receive_messages, args=(self,))
        receive_thread.start()

        self.root.mainloop()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client.send_message(message)
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.message_display.configure(state='normal')
        self.message_display.insert(tk.END, f"{message}\n")
        self.message_display.configure(state='disabled')
        self.message_display.see(tk.END)