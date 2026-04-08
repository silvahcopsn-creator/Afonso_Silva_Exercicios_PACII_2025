import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

def receber(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break

def enviar(sock):
    while True:
        msg = input()
        sock.send(msg.encode())

        if msg == "exit":
            break

def main():
    cliente = socket.socket()
    cliente.connect((HOST, PORT))

    nome = input("Nome: ")
    cliente.send(nome.encode())

    threading.Thread(target=receber, args=(cliente,)).start()
    threading.Thread(target=enviar, args=(cliente,)).start()

main()