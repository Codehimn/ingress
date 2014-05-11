import os
from selenium import webdriver
from time import sleep

# options = ChromeOptions()
# options.AddArgument("--user-data-dir=C:\\Users\\Codehimn\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# driver = ChromeDriver(options)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Codehimn\\AppData\\Local\\Google\\Chrome\\User Data\\selenium")
options.add_argument("--start-minimized")

chromedriver = "C:\\Users\\Codehimn\\Dropbox\\ingress\\selenium-2.41.0\\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver, chrome_options=options)

browser.get('https://accounts.google.com/signup')

browser.find_element_by_xpath('//*[@id="FirstName"]').send_keys('Juan')
browser.find_element_by_xpath('//*[@id="LastName"]').send_keys('Perez')

browser.find_element_by_xpath('//*[@id="GmailAddress"]').send_keys('ingress.acc10')
browser.find_element_by_xpath('//*[@id="Passwd"]').send_keys('iluminadopalma')
browser.find_element_by_xpath('//*[@id="PasswdAgain"]').send_keys('iluminadopalma')

browser.find_element_by_xpath('//*[@id="BirthDay"]').send_keys('01')
browser.find_element_by_xpath('//*[@id="BirthMonth"]/div/div[1]').click();
browser.find_element_by_xpath('//*[@id=":0"]/div').click();
browser.find_element_by_xpath('//*[@id="BirthYear"]').send_keys('1984')

browser.find_element_by_xpath('//*[@id="Gender"]/div/div[1]').click();
browser.find_element_by_xpath('//*[@id=":d"]').click();

browser.find_element_by_xpath('//*[@id="RecoveryEmailAddress"]').send_keys("codehimn@gmail.com");

browser.find_element_by_xpath('//*[@id="TermsOfService"]').click();
browser.find_element_by_xpath('//*[@id="recaptcha_response_field"]').click();

sleep(5)
i=0
while i < 100:
	sleep(0.5)
	i=+1
	# if 'done' in  browser.find_element_by_xpath('//*[@id="innerstatus"]/span[2]/span').text : i = 100
print('-done-')


# browser.execute_script('window.plugin.portalslist.displayPL()')

# print(str ( browser.find_element_by_xpath('//*[@id="portalslist"]').text() ) )
# print(browser.find_element_by_xpath('//*[@id="portalslist"]').value() )
# print(browser.find_element_by_xpath('//*[@id="portalslist"]').html() )
fuente = str ( browser.page_source )

# output = open('portales.list', 'w', encoding="UTF-8")
# output.write( fuente)
# output.close()

# browser.close()



# String imgmsg = driver.findElements(By.xpath("//div[@id='recaptcha_image']
#                  /img")).toString();
# System.out.println(imgmsg);