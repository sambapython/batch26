import socket
try:
	s=socket.socket()
	host=socket.gethostname()
	port = 8899
	s.connect((host,port))
	ack = s.recv(500)
	print ack
	num = raw_input("Enter number: ")
	s.send(num)
	response = s.recv(1024)
	print response
except Exception as err:
	print err
finally:
	s.close()