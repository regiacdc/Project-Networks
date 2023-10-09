from netmiko import ConnectHandler
#change github
iosv_l2 = {

    'device_type': 'cisco_ios',
    'ip': '192.168.1.155',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print (output)

#change lab-gitbuh
