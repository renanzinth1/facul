#lado ativo
import socket

HOST = 'localhost'
PORTA = 5000

#criar o descritor de socket
sock = socket.socket() #AF_INET, SOCK_STREAM

#estabelecer conexão
sock.connect((HOST, PORTA))

#enviar a mensagem de hello
sock.send(b'Ola, sou o lado ativo!')

#receber resposta do lado passivo
msg = sock.recv(1024)
print(str(msg, encoding='utf-8'))

#encerra a conexão
sock.close()
