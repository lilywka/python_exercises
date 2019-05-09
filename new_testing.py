from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1325x744')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')


driver = webdriver.Chrome(options=options)

driver.get('https://odessa.ithillel.ua/')
search_btn_xpath = "//nav[@class='main-navigation ']//a[@href = 'https://odessa.ithillel.ua/contact']"
driver.find_element_by_xpath(search_btn_xpath).click()

sleep(5)
number_tel1 = driver.find_element_by_id('contactPhone1').text
number_tel2 = driver.find_element_by_id('contactPhone2').text

assert '+38 (067) 121 09 96' == number_tel1, "Mobile phone number doesn't match.\nActual number: %s" % number_tel1
assert '+38 (048) 772 23 92' == number_tel2, "Landline phone number doesn't match\nActual number: %s" % number_tel2


driver.close()
