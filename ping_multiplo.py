import os
import time

with open('/home/cesar/python/projetos/dio/seguranca_da_informacao_python/host.txt',) as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ',ip)
        print('-' * 60)
        os.system(f'ping -n 2 {ip}')
        print('-' * 60)
        time.sleep(5)