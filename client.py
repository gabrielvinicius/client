import socket


class Client:
    def __init__(self, ip, port, username):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))
        self.client_socket.send(username.encode())

    def send_message(self, message):

        self.client_socket.send(message.encode())

    def receive_messages(self, chat_gui):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                chat_gui.display_message(message)
                print(message)
            except:
                self.client_socket.close()
                break

    def close_connection(self):
        self.client_socket.close()
