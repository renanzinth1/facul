# lado ativo
import socket
import os
import sys

HOST = 'localhost'
PORTA = 5000

# criar o descritor de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET, SOCK_STREAM

# estabelecer conexão
sock.connect((HOST, PORTA))
print("Conectado!")
print("= = = = = = = = = = = Renan Narciso = = = = = = = = = = =")
print('= = = = = = Sistema de transferência de arquivo = = = = =')
print("= 1 - Solicitar arquivo do servidor                     =")
print("= 2 - SAIR                                              =")
print("= = = = = = = = = = = = PPGI/UFRJ = = = = = = = = = = = =")

options = str(input("Selecione uma opção> "))

if options == "1":
    nomeArquivo = str(input("Digite o nome do arquivo> "))
    sock.send(nomeArquivo.encode())

    with open(nomeArquivo, 'wb') as file:
        while 1:
            data = sock.recv(1000000)
            file.write(data)
            if not data:
                msg = sock.recv(1024)
                print(str(msg, encoding='utf-8'))
                break
            print("Arquivo recebido!")
else:
    print("Encerrando sistema...")
    sys.exit()
