from selenium import webdriver
import urllib.request
import os

driver = webdriver.Chrome()
driver.get('https://dou.ua/')

logos_xpath = "//div[@class = 'items table']//div/a/img"
logos = driver.find_elements_by_xpath(logos_xpath)
driver.execute_script('window.scrollTo(0,500)')

directory = 'output'
if not os.path.exists(directory):
    os.makedirs(directory)

for i in logos:
    url = i.get_attribute('src')
    png = '{0}/{1}.png'.format(directory, i.get_attribute('alt'))
    urllib.request.urlretrieve(url, png)

driver.close()
