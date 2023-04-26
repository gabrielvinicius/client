import tkinter as tk
from tkinter import messagebox

from chat import ChatGUI



class ConnectGUI:
    def __init__(self,IP,PORTA):
        self.connect_window = tk.Tk()
        self.connect_window.title('Conectar')
        self.connect_window.geometry('300x200')

        # Campo de entrada para o endereço IP
        ip_label = tk.Label(self.connect_window, text='Endereço IP:')
        ip_label.pack(pady=5)
        self.ip_entry = tk.Entry(self.connect_window)
        self.ip_entry.insert(0, IP)
        self.ip_entry.pack()

        # Campo de entrada para a porta
        port_label = tk.Label(self.connect_window, text='Porta:')
        port_label.pack(pady=5)
        self.port_entry = tk.Entry(self.connect_window)
        self.port_entry.insert(0, PORTA)
        self.port_entry.pack()

        # Campo de entrada para o nome de usuário
        username_label = tk.Label(self.connect_window, text='Nome de Usuário:')
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.connect_window)
        self.username_entry.pack()

        # Botão para conectar
        connect_button = tk.Button(self.connect_window, text='Conectar', command=self.connect_to_server)
        connect_button.pack(pady=10)

        # Inicia a GUI
        self.connect_window.mainloop()

    def connect_to_server(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()

        if not ip or not port or not username:
            messagebox.showwarning('Aviso', 'Por favor, preencha todos os campos.')
            return

        try:
            port = int(port)
        except ValueError:
            messagebox.showwarning('Aviso', 'A porta deve ser um número inteiro.')
            return

        try:
            self.connect_window.destroy()
            chat_gui = ChatGUI(ip, port, username)
        except ConnectionRefusedError:
            messagebox.showwarning('Aviso', 'Não foi possivel se conectar no servidor')
            return


if __name__ == "__main__":
    connect_gui = ConnectGUI()
