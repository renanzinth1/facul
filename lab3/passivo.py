# lado passivo

import os.path
import socket
import select
import sys
import multiprocessing

entradas = [sys.stdin]
conexoes = {}

HOST = ''  # interface padrão de comunicação da máquina
PORTA = 10000  # identifica o processo na máquina

def iniciaServidor():
    # cria o descritor socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # internet e TCP

    # vincular o endereço e porta
    sock.bind((HOST, PORTA))

    # colocar em modo de despera
    sock.listen(7)  # argumento indica a qtde de conexões pendentes

    sock.setblocking(False)

    entradas.append(sock)
    return sock

def aceitaConexao(sock):
    # aceitar conexão
    novoSock, addr = sock.accept()

    # registra a nova conexao
    conexoes[novoSock] = addr

    return novoSock, addr

def atendeRequisicoes(novoSock, addr):
    while True:
        # recebe o nome do documento vindo do lado do cliente
        nomeArquivoRecv = novoSock.recv(1024)

        # recebe a palavra a ser buscada vindo do lado cliente
        palavraBuscadaRecv = novoSock.recv(1024)

        # pega o diretório atual
        # diretorioAtual = os.getcwd()

        # uni o diretório atual com o nome do arquivo, formando um caminho absoluto
        # filePath = os.path.join(diretorioAtual, nomeArquivoRecv)

        if not nomeArquivoRecv:
            print(str(addr) + '-> encerrou')
            novoSock.close()  # encerra a conexao com o cliente
            return
        else:
            if os.path.isfile(nomeArquivoRecv):
                arquivo = open(nomeArquivoRecv, mode='r')
                conteudo = arquivo.read()
                qntdBusca = conteudo.count(str(palavraBuscadaRecv, encoding='utf-8'))

                if qntdBusca > 0:
                    print(qntdBusca)
                    result = "Quantidade da palavra buscada encontrada no arquivo: " + str(qntdBusca) + " vez(es)."
                else:
                    result = "Palavra não encontrada no arquivo"
                arquivo.close()
            else:
                result = "Arquivo não encontrado!"

        # envia mensagem de resposta para o lado do cliente
        novoSock.send(bytes(result, 'utf-8'))

def main():

    clientes = []
    sock = iniciaServidor()

    print("Pronto para receber conexoes...")

    while True:
        r, w, e = select.select(entradas, [], [])

        # tratar todas as entradas prontas
        for pronto in r:
            if pronto == sock:  # pedido novo de conexao
                clisock, addr = aceitaConexao(sock)
                print('Conectado com: ', addr)

                cliente = multiprocessing.Process(target=atendeRequisicoes, args=(clisock, addr))
                cliente.start()
                clientes.append(cliente)

            elif pronto == sys.stdin:
                cmd = input()

                if cmd == 'fim':
                    for c in clientes:
                        c.join()

                    sock.close()
                    sys.exit()

                elif cmd == 'hist':
                    print(str(conexoes.values()))

main()
