from selenium import webdriver
import unittest
import codecs
import re


class PBList(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://privatbank.ua/')

    def test_pb_list(self):

        pb_string_xpath = "//ul[@class = 'nav nav-justified  navbar-nav']"
        pb_string = self.driver.find_elements_by_xpath(pb_string_xpath)
        pb_string = pb_string[0].text

        f = codecs.open("privat.txt", "r+", encoding='utf-8')
        s = (f.read())
        expected_pb_list = s.split('|')
        f.close()

        pb_string = re.sub(r'\n+', r' ', pb_string)
        for i in expected_pb_list:
            assert i in pb_string, "\nElement '{0}' was not found  in string '{1}'"\
                .format(i, pb_string)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
