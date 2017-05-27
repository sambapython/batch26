class emp:
	def __init__(self,name,age,sal,incp):
		self.name=name
		self.age=age
		self.sal=sal
		self.__incp = incp
	def sal_calc(self):
		try:
			return self.sal+self.sal*(self.__incp/100.0)
		except:
			return  None
