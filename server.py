import os
import socket
import subprocess
import _thread

def inputer():
	global p, h, pa
	p = 6999
	#p = int(input("Enter Port"))
	h = 'abc'
	#h = str(input("Enter Hostname"))
	pa = '123'
	#pa = str(input("Enter passsword"))

def init():
	global s
	inputer()
	s = socket.socket()
	s.bind(('127.0.0.1',p))
	s.listen(2)

def execute(cmd):
	with open('/tmp/Killer', "w") as outfile:
		subprocess.call(cmd, stdout=outfile)

def handler(conn, detail):
	print('New conn from : ' + detail[0] + ':' + str(detail[1]))
	d = conn.recv(1024).decode('utf-8')
	conn.sendall('1'.encode('utf-8'))
	passw = conn.recv(1024).decode('utf-8')
	
	if (pa == passw) and (h == d):
		conn.sendall('1'.encode('utf-8'))
		while True:
			r = conn.recv(1024).decode('utf-8')
			if r == 'exit':	
				break
			_thread.start_new_thread (execute, (r, ) )
			conn.sendall(otp)	
	else:
		conn.sendall('0'.encode('utf-8'))
	
	conn.close()

if __name__ == '__main__':
	init()
	#try:
	while True:
		conn, detail = s.accept()
		handler(conn, detail)
	#except:
	#	s.close()	
