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

block = raw_input("What IP address would you like to block? ")

config_set = ['object-group network THE_BAD_GUYS2', 'network-object host {block}'.format(**locals()), 'end']

for asa in (asas1, asa2):
    with ConnectHandler(**asa) as device:
        device.enable()
        device.config_mode()
        device.send_config_set(config_set, True)
        device.send_command_expect('wr')
        device.send_command_expect('logout')
    print asa
    
i = input("Press Enter to exit")
