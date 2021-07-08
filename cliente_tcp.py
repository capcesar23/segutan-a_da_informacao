'''
    Desenvolvimento de um cliente TCP
'''

import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou !!!')
        print(f'Erro: {e}')
        sys.exit()
    
    print('Socket criado com sucesso')

    HostAlvo = input('Digite o host ou ip a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com Sucesso no Host: ' + HostAlvo + " e na Porta: " + PortaAlvo )
        s.shutdown(2)
    except socket.error as erro:
        print('A conexão falhou. Não foi possivel conctar no Host: ' + HostAlvo + ' - Porta: ' + PortaAlvo )
        print(f'Erro: {erro}')
        sys.exit()

if __name__ == '__main__':
    main()