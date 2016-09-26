from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if len(sys.argv) > 1:
	idacc = sys.argv[1]

	#account 
	uid = '#email'.encode('hex')
	pid = '#password'.encode('hex')
	try:
		#create chrome
		driver = webdriver.Chrome('/media/kv/Data/python/webdriver/chromedriver')

		#access addr
		driver.get('https://www.fb.com')

		#title
		print driver.title

		#Login
		email = driver.find_element_by_id('email')
		email.send_keys(uid.decode("hex"))

		passwd = driver.find_element_by_id('pass')
		passwd.send_keys(pid.decode('hex'))
		passwd.send_keys(Keys.ENTER)

		#access addr
		driver.get('https://www.facebook.com/messages/' + idacc)

		#send message
		for i in range(100):
			mess = driver.find_element_by_name('message_body')
			mess.send_keys(':))) Test auto chat ' + str(i))
			mess.send_keys(Keys.ENTER)
	except:
		driver.close()
	
	#exit
	driver.close()
else:
	print 'id victim'


