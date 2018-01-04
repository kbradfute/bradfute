

from netmiko import ConnectHandler as ch

un = '<username>'
pw = '<password>'

cisco = {
    'device_type': 'cisco_ios',
    'ip': input('Enter the remote host\'s IP address or hostname: '),
    'username': un,
    'password': pw,
    }
asa = {
    'device_type': 'cisco_asa',
    'ip': input('Enter the remote ASA\'s IP address or hostname: '),
    'username': un,
    'password': pw,
    }
all_devices = [cisco, asa]
net_connect = ch(**cisco)

for a_device in all_devices:
    net_connect = ch(**a_device)    
    output = net_connect.send_command('show int')
    print(output)

end_time = datetime.now()
total_time = end_time - start_time
