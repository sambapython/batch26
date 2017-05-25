import socket
try:
	s=socket.socket()
	s.connect(("www.google.com",443))
	print "connected successfully"
except Exception as err:
	print err
finally:
	s.close()