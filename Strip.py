# The regex version of strip method.
# Strips input of space characters just like the strip string method
def RegexStrip():
	import re
	myRegex = re.compile(' ')
	string = input('Pls input something: ')
	# Substitute any space character and replace with nothing
	return myRegex.sub('', string)
print(RegexStrip())
	
	