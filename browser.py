import os
from selenium import webdriver
from time import sleep
from ingress_functions import *

read_portal_file()
exit(0)

# options = ChromeOptions()
# options.AddArgument("--user-data-dir=C:\\Users\\Codehimn\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# driver = ChromeDriver(options)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Codehimn\\AppData\\Local\\Google\\Chrome\\User Data\\selenium")
options.add_argument("--start-maximized")

chromedriver = "C:\\Users\\Codehimn\\Dropbox\\ingress\\selenium-2.41.0\\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver, chrome_options=options)

# browser.get('https://accounts.google.com/ServiceLogin')
# browser.find_element_by_xpath('//*[@id="Email"]').send_keys('ingress.acc6')
# browser.find_element_by_xpath('//*[@id="Passwd"]').send_keys('iluminadopalma')
# browser.find_element_by_xpath('//*[@id="signIn"]').click()

sleep(15)
i=0
while i < 120:
	sleep(0.5)
	i=+1
	if 'done' in  browser.find_element_by_xpath('//*[@id="innerstatus"]/span[2]/span').text : i = 900
print('-done-')

browser.execute_script('window.plugin.portalslist.displayPL()')

# print(str ( browser.find_element_by_xpath('//*[@id="portalslist"]').text() ) )
# print(browser.find_element_by_xpath('//*[@id="portalslist"]').value() )
# print(browser.find_element_by_xpath('//*[@id="portalslist"]').html() )
fuente = str ( browser.page_source )

output = open('portales.list', 'w', encoding="UTF-8")
output.write( fuente)
output.close()

browser.close()



read_portal_file()