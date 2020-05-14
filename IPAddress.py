
#Python Program to Get your IP Address

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Device name is:" + hostname)
print("Your Device IP Address is:" + IPAddr)
