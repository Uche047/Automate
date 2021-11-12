#! python3
# Program gets the category of pics to download  from imgur via the command line
import sys, bs4, requests, os
os.chdir('C:\\Users\\patri\\PycharmProjects\\Developper\\Pics')
# Concatenating input from command line terminal to imgur url and downloading with requests
res = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
# Checking for proper download
res.raise_for_status()
# Creating BeautifulSoup Object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# CSS selctor returning all a elements with img element within them
imlink = soup.select('a img')
# Looping through
for item in imlink:
    for i in range(len(imlink)):
        # Downloading links to searched pics
        try:
            res = requests.get('https:' + imlink[i].get('src'))
            res.raise_for_status()
        except:
            print('There was a problem')
        imgs = open(f'img_{i}.jpeg', 'wb')
        for chunk in res.iter_content(100000):
            imgs.write(chunk)
        imgs.close()
print('Done')