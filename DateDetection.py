# This code checks for valid dates between 1000 - 2999
import re
# Day Month and Year Regexes
Day = re.compile(r'^(0[1-9]|1[0-9]|2[0-9]|3[0-1])')
Month = re.compile(r'(/0[1-9]/|/1[0-2]/)')
Year = re.compile(r'(1\d\d\d)|(2\d\d\d)')
# Checking length of date
def checkLength(date):
	if len(date) == 10:
		return True
	return False
# Checking for months with maximum of 30 days
def MonthCheck2(date):
	xMonths = ['04', '06', '09', '11']
	if  date[0] + date[1] == '31':
		v = date[3] + date[4]
		if v in xMonths:
			return False
	return True	
# Checking for leap year and days allowed in February
def FebruaryCheck(date):
	Nondays= ['30', '31']
	if (date[3] + date[4]) == '02':
		u = date[0] + date[1]
		if u in Nondays:
			return False
		elif u == '29':
			yr = date[6] + date[7] + date[8] + date[9]
			year = int(yr)
#Checking if it is a leap yr. leap years are every year divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
			if year % 4 == 0:
				if (year % 100  and  year % 400) == 0:
					return True
				elif year % 100 != 0:
					return False
			else:
				return False
		elif u not in Nondays:
			return True
	return True
#Checking correct day input	
def checkDay(date):
	if Day.search(date) == None:
		return False
	return True
# Checking correct month input
def checkMonth(date):
	if  Month.search(date) != None:
		return True
	return False
	# Checking valid Year input
def checkYear(date):
	if Year.search(date) != None:
		return True
	return False
#Checking valid Date input
def ValidDate(date):
	if  not checkLength(date):
		return 'Invalid Date'
	if not MonthCheck2(date):
		return 'Invalid Date'
	if not FebruaryCheck(date):
		return 'Invalid Date'
	if not checkDay(date):
		return 'Invalid Date'
	if not checkMonth(date):
		return 'Invalid Date'
	if not checkYear(date):
		return 'Invalid Date'
	return 'Valid Date'
date = '29/02/2000'
print (ValidDate(date))
print(FebruaryCheck(date))

while True:
	print('Pls input a date in format DD/MM/YYYY')
	date = input()
	print(ValidDate(date))
	if  ValidDate(date) == 'Valid Date':
		break
	continue
