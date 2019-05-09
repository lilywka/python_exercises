from selenium import webdriver
import unittest


class TestNumberOne(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_new_york_first(self):
        self.driver.get('http://www.tankathon.com/')
        search_xpath = \
            "//td[text() = '1']/..//*[@class = 'desktop' and ../div]"

        search_first_number = str(self.driver.find_element_by_xpath(search_xpath).text)
        assert 'New York' == \
               search_first_number, '\nActual first number is "%s"\nExpected NewYork' % search_first_number

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
