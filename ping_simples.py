import os 
## importa o Módulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 60)## imprimindo # 60 vezes

ip_ou_host = input("Digite o IP ou HOST a ser verificado: ")
#criamos uma variavél que vai recebr do usuário um ip
print("-" * 60)## imprimindo - 60 vezes
os.system(f'ping -n 6 {ip_ou_host}')
## chamando o modulo systema da biblioteca ou modulo os 
# - comando ping -n -num de pacotes que serão 6 {}
print("-" * 60)## imprimindo - 60 vezes