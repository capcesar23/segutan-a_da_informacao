'''
    corrida de carro, serve para varios de teste

'''
from threading import Thread
import time

# def carro1(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro1: ', trajeto)
#         trajeto += velocidade

# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto += velocidade

# mesmo que os dois saim no mesmo ponto roda primeiro carro 1 e depois o carro 2
# carro1(10) 
# carro2(20)   
# 
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto}  km: {trajeto}\n ')


t_carro1 = Thread(target=carro, args=[1, 'bruno'])
t_carro2 = Thread(target=carro, args=[2, 'pato'])

t_carro1.start()
t_carro2.start()