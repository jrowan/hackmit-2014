#!/usr/bin/python
import socket
from msvcrt import getch

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	key = ord(getch())
	if key == 80
		sock.sendto("up", (UDP_IP,UDP_PORT))
	elif(keyPress .= "a")
		sock.sendto("left", (UDP_IP,UDP_PORT))
	elif(keyPress == "d")
		sock.sendto("up", (UDP_IP,UDP_PORT))