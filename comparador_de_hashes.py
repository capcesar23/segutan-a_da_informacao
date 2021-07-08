'''
Dica:
    bibilioteca Hashlib - imolementa uma interface comum
    para muitos algoritmos de hash seguro como SHA1, SHA256, 
    MD5 entre outros

    https://docs.python.org/
'''
import hashlib

arquivo1 = '/home/cesar/python/projetos/dio/seguranca_da_informacao_python/a.txt'
arquivo2 = '/home/cesar/python/projetos/dio/seguranca_da_informacao_python/b.txt'

hash1 = hashlib.new('ripemd160') # algoritmo de hash de 160 bits

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())
# digest  resumi os dados
if hash1.digest() != hash2.digest():
    print(f'O arquivo :\n\n {arquivo1}\n\n  é diferente do arquivo:\n\n {arquivo2}\n')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
else:
    print(f'O arquivo:\n \n{arquivo1}\n\n é igual ao\n\n {arquivo2}\n')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
