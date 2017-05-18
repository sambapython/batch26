import logging
logging.basicConfig(filename="log1.txt", level=logging.DEBUG, 
	format="%(asctime)s->%(levelname)s->%(message)s")

logging.info("*****Striting the client process***********")
a=raw_input("Enter a value:")
b=raw_input("enter b value: ")
logging.debug("a={0}, b={1}".format(a,b))
if not a.isdigit() or not b.isdigit():
	logging.warn("Expecting digits, getting: {0}, {1}".format(a,b))
try:
	a=float(a)
	b=float(b)
	res=a/b 
	logging.debug("result={0}".format(res))
	print "result=",res
except Exception as err:
	print "something went wrong"
	logging.exception(str(err))
