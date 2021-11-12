#! python3
# searchpypi.py - Open several search results
import bs4, requests, sys, webbrowser
print("Searching....") # Display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()