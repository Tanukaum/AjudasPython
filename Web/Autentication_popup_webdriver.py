import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#user:password
url = 'http://admin:admin@endereço/'
options = Options()
options.headless = False #False = Open Window, True = Open Hide Mode

driver = webdriver.Firefox(options=options)
driver.get(url)
print(driver)
time.sleep(10)
driver.close()