#! python3
# 2048.py opens a website using selenium and automatically plays the game
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Opening Chrome with selenium
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
for i in range(50):
    # Automating Up, Right, Down, Left clicks 50 times
    htmlElement = browser.find_element_by_tag_name('html')
    htmlElement.send_keys(Keys.UP)
    htmlElement.send_keys(Keys.RIGHT)
    htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
