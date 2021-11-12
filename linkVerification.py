#! python3
# This program gets all the links on a webpage verifies and downloads them
import requests, bs4, os
os.chdir('C:\\Users\\patri\\PycharmProjects\\Developper\\HTML')
# Downloading info from goal.com/en
res = requests.get('https://goal.com/en')
# Checks that the download was hitch free
res.raise_for_status()
# Creating a beautiful soup object
goalSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# Returning a list with all a elements on the site
links = goalSoup.select('a')
# Looping through the list
for item in links:
    for i in range(len(links)):
        # Concatenating to get complete links
        newLink = 'https://goal.com' + links[i].get('href')
        try:
            # Downloading all new links previously concatenated with requests
            res = requests.get(newLink)
            res.raise_for_status()
            # Opening a html file object in write binary mode and getting the base name of the links 
            # Also concatenating to add the .html suffix 
            htmlFile = open(os.path.basename(newLink) +'.html', 'wb')
            for chunk in res.iter_content(100000):
                htmlFile.write(chunk)
            htmlFile.close()
        except Exception as exc:
            print('There was a problem connecting %s' %(exc))
