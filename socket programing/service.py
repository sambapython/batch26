import socket
try:
	s=socket.socket()
	host = socket.gethostname()
	port = 8899
	s.bind((host,port))
	s.listen(6)
	print "waiting for the requests"
	co, ci = s.accept()
	co.send("connection established well")
	num = co.recv(10)
	resp = "ODD"
	if int(num)%2==0:
		resp="EVEN"
	co.send(resp)
except Exception as err:
	print err
finally:
	print "closing the socket"
	s.close()