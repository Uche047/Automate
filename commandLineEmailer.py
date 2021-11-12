#! python3
# This program sends a mail to an address 
# when provided the destination email and message in that order
# Making the neccessary imports
import sys, time
import pyinputplus as pyip
from selenium import webdriver
browser = webdriver.Chrome()
# Opening the yahoomail Login Page
browser.get('https://mail.yahoo.com/d/compose')
elem = browser.find_element_by_class_name('phone-no')
# Using time module to make program behave like a human
time.sleep(8)
# Inputing your email
elem.send_keys('patrickuchedjpms@yahoo.com')
nextbutton = browser.find_element_by_name('signin')
time.sleep(5)
# Clicking to next web page
nextbutton.click()
# Prompting for passwords
password = pyip.inputPassword('Pls input your yahoomail password: ')
passElem = browser.find_element_by_name('password')
time.sleep(10)
passElem.send_keys(password)
nextbutton = browser.find_element_by_name('verifyPassword')
time.sleep(15)
# Sending the password and login in
try:
    nextbutton.click()
except:
    print('There was a minor handshake error')
# Finding email element
email = browser.find_element_by_id('message-to-field')
time.sleep(5)
# Using email supplied from the command line
email.send_keys(sys.argv[1])
# Finding subject element
subject = browser.find_elements_by_tag_name('input')
# Sending Subject of mail
subject[10].send_keys('Automated Mail')
# Finding body element
body = browser.find_element_by_class_name('rte ')
time.sleep(20)
# Sending message supplied from the command line
body.send_keys(" ".join(sys.argv[2:]))
send = browser.find_element_by_class_name('q_Z2aVTcY')
# Time delay before sending the mail
time.sleep(15)
# Sending the mail now Whew!!!
send.click()
