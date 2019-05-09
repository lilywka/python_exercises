from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://odessa.ithillel.ua/')
search_btn_xpath = "//nav[@class='main-navigation ']//a[@href = 'https://odessa.ithillel.ua/contact']"
driver.find_element_by_xpath(search_btn_xpath).click()

driver.get_screenshot_as_file('pic.png')
driver.save_screenshot('pic.png')

number_tel1 = driver.find_element_by_id('contactPhone1').text
number_tel2 = driver.find_element_by_id('contactPhone2').text

assert '+38 (067) 121 09 96' == number_tel1, "Mobile phone number doesn't match"
assert '+38 (048) 772 23 92' == number_tel2, "Landline phone number doesn't match"

driver.close()
