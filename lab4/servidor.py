# lado passivo
import socket
import os.path

HOST = ''  # interface padrão de comunicação da máquina
PORTA = 5000  # identifica o processo na máquina

# cria o descritor socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # internet e TCP

# vincular o endereço e porta
sock.bind((HOST, PORTA))

# colocar em modo de despera
sock.listen(1)  # argumento indica a qtde de conexões pendentes

cliente, addr = sock.accept()

nomeArquivo = cliente.recv(1024).decode()

isFile = os.path.isfile(nomeArquivo)

if isFile:
    with open(nomeArquivo, 'rb') as file:
        for data in file.readlines():
            cliente.send(data)
            print("Arquivo enviado!")
else:
    cliente.send(bytes("Arquivo não encontrado!", 'utf-8'))
    print("Arquivo não encontrado!")
