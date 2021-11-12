# This program prompts customers to make choices that help to build the customer's sandwich and returns the price '
import pyinputplus as pyip
menuDict = {'wheat':2, 'white':1.5, 'sourdough': 1.7, 'chicken':7, 'turkey':10, 'ham':5, 'tofu':4.5, 'cheddar':1.7, 'swiss':1.5, 'mozzarella':2, 'mayo':0.7, 'mustard':1.1, 'lettuce':2.0, 'tomato':2.5, 'empty':0 }
# prompt to  ask the customer choice for bread
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
# prompt to  ask the customer choice for protein
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
# prompt to  ask the customer choice for cheese
choice1 = pyip.inputYesNo(prompt= 'Pls input Yes or No if you would like cheese: ')
if choice1 == 'yes':
	cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered = True)
else:
	cheese = 'empty'
# prompt to  ask the customer choice for vegetable
choice2 = pyip.inputYesNo(prompt= 'Pls input Yes or No if want vegetable : ')
if choice2 == 'yes':
	vegetable = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
else:
	vegetable = 'empty'
noOfSandwiches = pyip.inputInt(prompt= 'Please input the number of sandwiches you desire: ', min=1)
sum = menuDict[bread] + menuDict[protein] + menuDict[cheese] + menuDict[vegetable]
totalCost = noOfSandwiches * sum
print ()
print('You ordered %s sandwiches and that sums to $%s'  %(noOfSandwiches, totalCost))