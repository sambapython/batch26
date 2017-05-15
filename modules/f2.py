
a=100
b=200
c=300
def fun2():
	return  "this is fun2 in f2"
	
def fun():
	return "this is fun in f2"

if __name__=="__main__":
	def fun1():
		return "this is fun1 in f2"

	print "some starting statements"
	print "name golbal attribute value: ",__name__
	print "calling fun"
	print fun1()
	print fun()
	print "some ending statements"
