from selenium import webdriver
import unittest
import codecs


class PBList(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://privatbank.ua/')

    def test_pb_list(self):

        pb_list_xpath = "//ul[@class = 'nav nav-justified  navbar-nav']"
        pb_list = self.driver.find_elements_by_xpath(pb_list_xpath)

        new_pb_list = []
        for i in pb_list:
            new_pb_list.append(i.text)
        new_pb_list = new_pb_list[0].split('\n')
        new_pb_list.extend(new_pb_list[7].split(' '))

        f = codecs.open("privat.txt", "r+", encoding='utf-8')
        s = (f.read())
        expected_pb_list = s.split('|')
        f.close()

        actual_pb_list = []
        for item in new_pb_list:
            if item in expected_pb_list:
                actual_pb_list.append(item)
        assert expected_pb_list == actual_pb_list, "\nExpected result: {0}\nActual result:{1}" \
            .format(expected_pb_list, actual_pb_list)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
