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

# Comando para fazer "shutdown" em uma interface (altere a interface conforme necessário)
interface_name = 'interface GigabitEthernet0/1'
shutdown_command = f'{interface_name}\nshutdown'

# Envie o comando de "shutdown"
output = net_connect.send_config_set(shutdown_command)

# Imprima a saída para verificação
print(output)

# Feche a conexão
net_connect.disconnect()