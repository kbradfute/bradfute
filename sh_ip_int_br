

from netmiko import ConnectHandler as ch

cisco = {
    'device_type': 'cisco_ios',
    'ip': input('Enter the remote host\'s IP address or hostname: '),
    'username': '<your username here>',
    'password': '<your password here>',
    }

net_connect = ch(**cisco)

output = net_connect.send_command('show ip int br')
print(output)
