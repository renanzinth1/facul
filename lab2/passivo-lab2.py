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
sock.listen(7)  # argumento indica a qtde de conexões pendentes

# aceitar conexão
novoSock, endereco = sock.accept()
print('Conectado com:' + str(endereco))


def ehUmArquivo(filePath):
    os.path.isfile(filePath)

while True:
    # recebe o nome do documento vindo do lado do cliente
    nomeArquivoRecv = novoSock.recv(1024)

    # recebe a palavra a ser buscada vindo do lado cliente
    palavraBuscadaRecv = novoSock.recv(1024)

    # pega o diretório atual
    diretorioAtual = os.getcwd()

    # uni o diretório atual com o nome do arquivo, formando um caminho absoluto
    filePath = os.path.join(diretorioAtual, nomeArquivoRecv)

    if not nomeArquivoRecv:
        break
    else:
        if ehUmArquivo(filePath):

            arquivo = open(filePath, mode='r')
            conteudo = arquivo.read()

            qntdBusca = conteudo.count(str(palavraBuscadaRecv, encoding='utf-8'))
            
            if qntdBusca > 0:
                result = "Quantidade da palavra buscada encontrada no arquivo: " + str(qntdBusca) + " vez(es)."
            else:
                result = "Palavra não encontrada no arquivo"
            arquivo.close()
            
        else:
            result = "Arquivo não encontrado!"

    # envia mensagem de resposta para o lado do cliente
    novoSock.send(bytes(result, 'utf-8'))

# fecha o socket principal
sock.close()
