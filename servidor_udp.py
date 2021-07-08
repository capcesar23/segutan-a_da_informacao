import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host = 'localhost'
port = 5432

s.bind((host, port))
mensage = '\nServidor: Olá Cliente e aí '

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensage.encode()), end)