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

# Acesse o modo de configuração privilegiada
net_connect.enable()

# Comando para copiar o novo IOS para o switch (substitua pelos detalhes do seu arquivo IOS)
ios_file = 'c3750e-universalk9-mz.152-2.E.bin'  # Nome do arquivo IOS
copy_command = f'copy tftp://{seu_servidor_tftp}/{ios_file} flash:'

# Envie o comando de cópia do IOS
output = net_connect.send_command_timing(copy_command)

# Confirme a cópia do arquivo (substitua 'confirm' pelo texto apropriado)
if 'confirm' in output.lower():
    output += net_connect.send_command_timing('y')

# Imprima a saída para verificação
print(output)

# Comando para configurar o switch para usar o novo IOS após a reinicialização
config_commands = [
    'boot system flash:/c3750e-universalk9-mz.152-2.E.bin',  # Substitua pelo nome do seu arquivo IOS
    'write memory',  # Salvar a configuração
]

# Envie os comandos de configuração
output = net_connect.send_config_set(config_commands)

# Imprima a saída para verificação
print(output)

# Comando para reiniciar o switch
reboot_command = 'reload'
output = net_connect.send_command_timing(reboot_command)
if 'confirm' in output.lower():
    output += net_connect.send_command_timing('y')

# Imprima a saída para verificação
print(output)

# Feche a conexão
net_connect.disconnect()