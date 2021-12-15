# lado passivo

import os.path
import select
import sys
import multiprocessing

from lab3.RequestService import iniciaServidor, aceitaConexao, atendeRequisicoes

entradas = [sys.stdin]
conexoes = {}

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
