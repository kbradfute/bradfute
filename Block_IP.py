from netmiko import ConnectHandler

asa1 = {
    'device_type': 'cisco_asa',
    'ip': '10.0.0.1',
    'username': 'username',
    'password': 'supersecretpassword',
    'secret': 'superdupersecretpassword',
    'port': 22,
}

asa2 = {
    'device_type': 'cisco_asa',
    'ip': '10.0.0.2',
    'username': 'username',
    'password': 'supersecretpassword',
    'secret': 'superdupersecretpassword',
    'port': 22,
}

block = raw_input("What IP address would you like to block?")

config_set = ['object-group network THE_BAD_GUYS2', 'network-object host {block}', 'end']

for asa in (asas1, asa2):

net_connect = ConnectHandler(**asa)
output = net_connect.send_command_expect('show ip')
print output

net_connect.disconnect()

i = input("Press Enter to exit")
