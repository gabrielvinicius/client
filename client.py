import socket


class Client:
    def __init__(self, ip, port, username):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip, port))
        self.client_socket.send(username.encode())

        # Inicia uma thread para receber mensagens do servidor
        # threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        """
        Envia uma mensagem para o servidor.
        """
        self.client_socket.send(message.encode())

    def receive_messages(self, chat_gui):
        """
        Recebe mensagens do servidor e imprime na tela.
        """
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                chat_gui.display_message(message)
                print(message)
            except:
                self.client_socket.close()
                break
