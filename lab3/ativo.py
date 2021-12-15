# lado ativo
import socket
import os

HOST = 'localhost'
PORTA = 5000

# criar o descritor de socket
sock = socket.socket()  # AF_INET, SOCK_STREAM

# estabelecer conexão
sock.connect((HOST, PORTA))

nomeArquivo = input("Buscar por nome de arquivo [s = sair]: ")

# isfile = os.path.isfile(nomeArquivo)
# if isfile:
#     print(isfile)
#     arq = open(nomeArquivo, mode='r')
#     linhas = arq.readlines()
#
#     for linha in linhas:
#         print(linha)
# else:
#     print(isfile)

while nomeArquivo != 'sair':

    palavraBuscada = input("Informe a palavra a ser buscada no arquivo: ")

    # envia o nome do arquivo para o lado passivo
    sock.send(bytes(nomeArquivo,'UTF-8'))

    # envia a palavra buscada para o lado passivo
    sock.send(bytes(palavraBuscada,'UTF-8'))

    msg = sock.recv(1024)

    # mostra a mensagem recebida
    print(str(msg,  encoding='utf-8'))

else:
    # encerra a conexao
    sock.close()
    print("\n\n\nConexão interrompida...")
