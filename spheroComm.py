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

while True:
		data, addr = sock.recvfrom(1024)
		print "received message:", data

from sphero_driver import sphero_driver
import sys
sphero = sphero_driver.Sphero()
sphero.connect()
sphero.set_raw_data_strm(40, 1 , 0, False)

sphero.start()

time.sleep(2)
sphero.roll(255,0,1,False)
time.sleep(2)
sphero.roll(0,0,0,False)
sphero.join()
sphero.disconnect()
sys.exit(1)