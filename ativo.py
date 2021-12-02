# lado ativo
import socket

HOST = 'localhost'
PORTA = 5000

# criar o descritor de socket
sock = socket.socket()  # AF_INET, SOCK_STREAM

# estabelecer conexão
sock.connect((HOST, PORTA))

numMsg = 0

while True:

    val = input("Deseja continuar recebendo echo [S/N]?")

    if val == 'S' or val == 's':
        # envia mensagem para o lado passivo
        sock.send(b'Ola, sou o lado ativo!')

        # recebe resposta do lado passivo
        msg = sock.recv(1024)
        numMsg: int = numMsg + 1
        print("\nMensagem recebida nº(%d): " %numMsg)
        print(str(msg, encoding='utf-8'))

    if val == 'N' or val == 'n':
        # encerra a conexão
        sock.close()
        print("\n\n\nConexão interrompida...")
        break
