'''
    Desenvolvimento de um cliente UDP
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # objeto de conexão

print('Cliente Socket Criado com Sucesso !!!')

host = 'localhost'
porta = 5433
mensagem = 'Finalmente nos encontramos'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) # empacotar e enviar no host e porta

    dados, servidor = s.recvfrom(4096) # ira receber a resposta do servidor
    dados = dados.decode() # irá desempacotar os dados
    print('Cliente: ' + dados )

finally:
    print('Cliente: Fechando a conexão')
    s.close()