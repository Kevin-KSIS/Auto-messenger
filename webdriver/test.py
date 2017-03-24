##############################################################
# requires lib: selenium
# System os: linux
# Browser: chrome
# version: python 3 or later
# website: messenger.com
##############################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if len(sys.argv) > 1:
	id = sys.argv[1]

	#account 
	uid = ''
	pid = ''
	try:
		#create chrome session
		driver = webdriver.Chrome('./chromedriver')
		
		#access address
		#driver.get('https://www.fb.com')
		driver.get('https://www.messenger.com' + id)
		print(driver.title)

		#Login
		email = driver.find_element_by_id('email')
		email.send_keys(uid)
		passwd = driver.find_element_by_id('pass')
		passwd.send_keys(pid)
		passwd.send_keys(Keys.ENTER)

		#send message
		for i in range(100):
			mess = driver.find_elements_by_class_name("message_body")
			mess.send_keys(':))) Test auto chat ' + str(i))
			mess.send_keys(Keys.ENTER)
	except:
		print('err')
		driver.close()
else:
	print('python autochat.py idvictim')


