import socket
import threading
from gdpr_utils import detectar_dados

HOST = '127.0.0.1'
PORT = 5555

clientes = []

def broadcast(msg, conn):
    for c in clientes:
        if c != conn:
            try:
                c.send(msg.encode())
            except:
                pass

def cliente_thread(conn, addr):
    print("Cliente ligado:", addr)

    nome = conn.recv(1024).decode()
    clientes.append(conn)

    broadcast(nome + " entrou no chat", conn)

    while True:
        try:
            msg = conn.recv(1024).decode()

            if msg == "exit":
                break

            dados = detectar_dados(msg)

            if dados:
                conn.send("Mensagem bloqueada (dados pessoais)".encode())
                continue

            broadcast(nome + ": " + msg, conn)

        except:
            break

    clientes.remove(conn)
    broadcast(nome + " saiu do chat", conn)
    conn.close()

def main():
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()

    print("Servidor a correr...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=cliente_thread, args=(conn, addr)).start()

main()  