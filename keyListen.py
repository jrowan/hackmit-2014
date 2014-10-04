#!/usr/bin/python
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, world!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendTo(MESSAGE, (UDP_PORT,UDP_IP))