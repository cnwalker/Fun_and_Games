from random import randint

class Birthday(object):
	def _init_(self):
		self.month = 0
		self.day = 0
		self.year = 0
		
	def month_day(self):
		return str(self.month) + "," + str(self.day)
		
def leap_year(year):
	if year % 4 == 0 and year % 100 != 0:
		return True
	else:
		return False
		
def get_day(month, year):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return randint(1, 31)
	if month in [4, 6, 9, 11]:
		return randint(1, 30)
	if month == 2:
		if leap_year(year):
			return randint(1, 29)
		else:
			return randint(1, 28)
	
def generateBirthday():
	m = randint(1, 12)
	y = randint(1890, 2014)
	b = Birthday()
	b.month = m
	b.day = get_day(m, y)
	b.year = y
	return b
	
def testparadox(pnum):
	blist = []
	for i in range(0, pnum): 
		blist.append(generateBirthday().month_day())
		
	
	if len(set(blist)) < len(blist):
		return True
	else:
		return False
		
def get_percent(pnum, trials):
	s = 0.0
	for i in range(0, trials):
		if testparadox(pnum) == True:
			s += 1
	return s/trials
