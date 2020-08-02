# from https://www.tutorialspoint.com/python-program-to-find-the-ip-address-of-the-client

import socket, ipaddress, sh
from requests import get

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)  # My ip

# Router IP from https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python


router_ip = get('https://api.ipify.org').text

# ip of all devices connected to router

network_object = ipaddress.ip_network(ip_address)
# get the subnets list(network_object.subnets()))

# https://itsfoss.com/how-to-find-what-devices-are-connected-to-network-in-ubuntu/
# To do figure out how to list all addresses connected to my router

print(router_ip, ip_address)

# https://www.c-sharpcorner.com/article/python-program-to-find-all-ip-assigned-in-a-network/
for num in range(105, 115):
    ip = "192.168.0." + str(num)
    
    try:
        sh.ping(ip, "-c 1")
        print("PING ", ip, "OK")
    except sh.ErrorReturnCode_1:
        print("PING ", ip, "FAILED")
