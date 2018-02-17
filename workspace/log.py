from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from urllib import request
from time import sleep
from user import User

class Log:

	host = "https://www.google.com"
	link = "https://1.1.1.1/login.html"

	#check if you are connected to the network...
	def check_host():
	    connected = True
	    while(connected):
	        try:
	        	with request.urlopen(link, timeout=5) as response:
		            if response.code==200: #ok, conected
		                print('conectado...')
		     		else:
		     			print(response.code)
	        except:
	            __re_login()
	            connected = False
	            pass
	        sleep(5)

	    a.close()

	#fill in the form on the variable 'link'
	def __re_login():
	    m_user = User.get_instance()

	    driver = webdriver.PhantomJS()
	    driver.get(link)

	    username = driver.find_element_by_name("username")
	    password = driver.find_element_by_name("password")
	    button = driver.find_element_by_name("Submit")

	    username.clear()
	    password.clear()

	    username.send_keys(m_user.login)
	    password.send_keys(m_user.password)
	    button.click()

	    driver.close()