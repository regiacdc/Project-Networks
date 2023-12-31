import paramiko
import re

switches = ["192.168.1.128", "192.168.1.127", "192.168.1.130", "192.168.1.154", "192.168.1.155", "192.168.1.156", "192.168.1.157"]


username = "cisco"
password = "cisco"

def get_loopback_interfaces_with_ip(ip, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(ip, username=username, password=password, timeout=10)
        stdin, stdout, stderr = ssh_client.exec_command("show ip interface brief | include Loopback")
        output = stdout.read().decode('utf-8')

        
        loopback_info = re.findall(r'Loopback\d+.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', output)

        return loopback_info

    except paramiko.AuthenticationException:
        print(f"Error de autenticación en {ip}")
    except paramiko.SSHException as e:
        print(f"Error de conexión SSH en {ip}: {str(e)}")
    except Exception as e:
        print(f"Error inesperado en {ip}: {str(e)}")
    finally:
        ssh_client.close()

for switch_ip in switches:
    print(f"Interfaces Loopback {switch_ip} e IP:")
    loopback_info = get_loopback_interfaces_with_ip(switch_ip, username, password)
    
    if loopback_info:
        for info in loopback_info:
            print(info)
    else:
        print("No se encontraron interfaces Loopback en este switch.")


