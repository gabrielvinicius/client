# This is a sample Python script.
from conect import ConnectGUI
import os
from dotenv import load_dotenv

load_dotenv()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#  print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#  print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Inicia a tela de conexão

if __name__ == "__main__":
    connect_gui = ConnectGUI(os.environ['IP'],os.environ['PORTA'])

