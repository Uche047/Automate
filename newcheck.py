totalVisitors =  {'Ikpom': {'chickenlaps': 9, 'eggs': 56},
 'Patrick': {'spaghetti': 12, 'milk': 5},
 'Ediale': {'eclairs': 45, 'apples': 10}}
def totalDonation(visitors, item):
	numDonation = 0
	for k, v in visitors.items():

		numDonation = numDonation + v.get(item)
		return numDonation

print(' - chickenlaps ' , totalDonation(totalVisitors, 'chickenlaps'))