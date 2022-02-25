import time
import socket
# pyinstaller 명령어
# D:\dev\github\sixty_coding\test> pyinstaller -F socket_getaddrinfo.py

socket_test = socket.getaddrinfo('localhost', 5555)
time.sleep(5)
print(socket_test)
time.sleep(5)
