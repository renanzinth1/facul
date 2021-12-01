#lado passivo
import socket

HOST = '' #interface padrão de comunicação da máquina
PORTA = 5000 #identifica o processo na máquina

#cria o descritor socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #internet e TCP

#vincular o endereço e porta
sock.bind((HOST, PORTA))

#colocar em modo de despera
sock.listen(1) #argumento indica a qtde de conexões pendentes

#aceitar conexão
novoSock, endereco = sock.accept()
print('Conectado com:' + str(endereco))

while True:
    #esperar por mensagem do lado ativo
    msg = novoSock.recv(1024) #argumento indica qtde máxima de bytes
    if not msg: break
    print(str(msg, encoding='utf-8'))
    novoSock.send(b'Ola, sou o lado passivo!')
    
#fechar o descritor de socket da conexão
novoSock.close()
