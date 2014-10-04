#!/usr/bin/python
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
MESSAGE = "Hello, world!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))