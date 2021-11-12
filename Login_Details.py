tries = 0
while tries<=3: 
    print('Who are you?')
    tries= 1 + tries
    name = input()  
    if name != 'Joe':
      print("Invalid user")
      continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input() 
    if password == 'swordfish':
      print('Access granted.')
    else:
    	print ('Wrong password')
    	continue
      
    break
