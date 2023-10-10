from netmiko import ConnectHandler

# Defina os parâmetros de conexão para o dispositivo Cisco
device = {
    'device_type': 'cisco_ios',
    'ip': 'seu_endereco_ip',
    'username': 'seu_nome_de_usuario',
    'password': 'sua_senha',
    'secret': 'sua_senha_privilegiada',  # Se necessário
}

# Conecte-se ao dispositivo
net_connect = ConnectHandler(**device)

# Acesse o modo de configuração
net_connect.enable()

# Comandos de configuração para atualização (substitua pelos comandos relevantes)
config_commands = [
    'interface GigabitEthernet0/1',
    'description Nova descrição',
    'ip address 192.168.1.1 255.255.255.0',
    'no shutdown',
    'exit',
]

# Envie os comandos de configuração para atualização
output = net_connect.send_config_set(config_commands)

# Imprima a saída para verificação
print(output)

# Feche a conexão
net_connect.disconnect()