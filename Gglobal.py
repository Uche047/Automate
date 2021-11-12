"""
def spam():
	global eggs
	eggs = 'spam'
eggs = 'global'
spam()
#eggs = 'global'
print(eggs)
"""
"""
def spam():
	global eggs
	eggs = "spam"
def bacon():
	eggs = 'bacon' # local
def ham():
	print(eggs)
eggs = 42
spam()
print(eggs)
"""
def spam():
	print(eggs)# Error
	eggs = "spam local"
eggs = "global"
spam()