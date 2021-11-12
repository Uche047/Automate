from FantasyGameInventory import displayInventory
def addToInventory(inventory, addedItems):
	for i in addedItems:
		if i in inventory:
			inventory[i] += 1
		
		else:
			inventory [i] = 1
	return inventory

inv = { 'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'dagger', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)