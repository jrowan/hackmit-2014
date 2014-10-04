#!/usr/bin/python
import bluetooth
import struct
import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


from sphero_driver import sphero_driver
import sys
sphero = sphero_driver.Sphero()
sphero.connect()
sphero.set_raw_data_strm(40, 1 , 0, False)

sphero.start()

while True:
		data, addr = sock.recvfrom(1024)
		if data == "left"
			sphero.roll(100,270,1,False)
		elif data == "right"
			sphero.roll(100,90,1,False)
		elif data == "up"
			sphero.roll(100,0,1,False)
		else
			sphero.roll(0,0,0,False)

sphero.join()
sphero.disconnect()
sys.exit(1)