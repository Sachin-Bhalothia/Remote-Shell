import os
import socket

IP = '127.0.0.1'

def init():
	global s, h, p
	s = socket.socket()
	h = 'abc'
	#h = input("Enter hostname")
	p = '123'
	#p = input("Enter Password")
	s.connect((IP,6999))
	s.send(h.encode('utf-8'))
	
def comute():
	v = str(s.recv(1024).decode('utf-8'))
	if v == '1':
		s.send(p.encode('utf-8'))
		ch = str(s.recv(1024).decode('utf-8'))
		if ch ==  '1':
			while True:
				i = input(h + '@' + IP + ':')
				if i == 'exit':
					break
				s.send(i.encode('utf-8'))
				r = str(s.recv(1024).decode('utf-8'))
				print(r)	
		else:
			print('Error : Password error , Enter Correct Password')
	else:
		print('Error : Hostname error , Enter Correct Hostname')
if __name__ == '__main__':
	init()
	comute()
