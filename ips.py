import ipaddress

ip = '192.168.0.1'

rede = '192.168.0.0/24'

redes = ipaddress.ip_network(rede)

endereco = ipaddress.ip_address(ip)

for rede in redes:
    print(rede)
#print(endereco + 100) # pode fazer somatario com os ip endereco + 100