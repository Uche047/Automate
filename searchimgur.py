#! python3
# searchpypi.py
import requests, sys, webbrowser, bs4, os
print('Searching...')   # display text downloading the search result page
res = requests.get('https://imgur.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
os.makedirs('searchPics', exist_ok=True)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.image-list-link')
print(linkElems)
# LinkElems is a list that returns 
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	urlToOpen = 'https://imgur.com' + linkElems[i].get('href')
	print('Opening', urlToOpen)
	webbrowser.open(urlToOpen)
	rest = requests.get('https:' + linkElems[i].get('src'))
	rest.raise_for_status()
	
	imageFile = open(os.path.join('searchPics', os.path.basename('https:' + linkElems[i].get('src'))), 'wb')
	for chunk in rest.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()
