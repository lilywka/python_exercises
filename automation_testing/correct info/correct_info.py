from selenium import webdriver
import unittest


class CorrectInfo(unittest.TestCase):

    def go_to_detailed_info(self):
        xpath_address = "//span[text() = 'Адреса доставки']/..//div/a"
        a = self.driver.find_element_by_xpath(xpath_address).get_attribute('href')
        self.driver.get(a)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get('https://novaposhta.ua')
        self.driver.find_element_by_id('cargo_number').send_keys('20400118411761\n')

    def test_np_route(self):

        xpath_route = "// span[text() = 'Маршрут'] /..// div"
        np_route = str(self.driver.find_element_by_xpath(xpath_route).text)
        route = 'Київ - Одеса'
        assert route == np_route, '\nExpected route: {0}\nActual route is: {1}' .format(route, np_route)

    def test_number_np_address(self):
        xpath_address = "//span[text() = 'Адреса доставки']/..//div/a"
        np_address = str(self.driver.find_element_by_xpath(xpath_address).text)
        expected_np_address = 'Відділення №37 (до 30 кг): вул. Олександра Невського, 57'
        assert expected_np_address == np_address, '\nExpected address: {0}\nActual address: {1}'\
            .format(expected_np_address, np_address)

    def test_address(self):
        self.go_to_detailed_info()

        expected_list = ['Відділення №37', 'Адреса: вул. Олександра Невського, 57', 'Тип: Поштове відділення',
                         'Обмеження ваги: До 30 кг']

        info_np_37_xpath = "//div[@class = 'text']"
        np_37 = self.driver.find_elements_by_xpath(info_np_37_xpath)

        actual_list = []
        for item in np_37:
            actual_list.append(item.text)

        actual_list = actual_list[0].split('\n')
        assert expected_list == actual_list, \
            "\nExpected list: {0} \nActual list: {1}".format(expected_list, actual_list)

    def test_time_table(self):
        self.go_to_detailed_info()
        info_time_table_xpath = "//div[@class = 'time_table clearfix']//tbody//td/span" \
                                "[@class = 'timeline-i']/../.."
        time_table = self.driver.find_elements_by_xpath(info_time_table_xpath)
        expected_list = ['Графік роботи', '08:00-21:00', '08:00-21:00', '08:00-21:00',
                         '08:00-21:00',	'08:00-21:00',	'09:00-18:00',	'11:00-16:00']
        actual_list = []
        for item in time_table:
            actual_list.append(item.text)
        actual_list = actual_list[0].split('\n')
        actual_list = [actual_list[0]] + actual_list[1].split()

        assert expected_list == actual_list,\
            "\nExpected list: {0} \nActual list: {1}".format(expected_list, actual_list)

    def test_time_departure(self):
        self.go_to_detailed_info()
        info_time_departure_xpath = "//div[@class = 'time_table clearfix']//tbody//td/span" \
                                    "[@class = 'timedeparture-i']/../.."
        time_departure = self.driver.find_elements_by_xpath(info_time_departure_xpath)

        expected_list = ['Прийом відправлення для відправки в той же день',
                         'До 15:30', 'До 15:30', 'До 15:30', 'До 15:30',
                         'До 15:30', 'До 15:30', 'До 15:25']

        actual_list = []
        for item in time_departure:
            actual_list.append(item.text)

        actual_list = actual_list[0].split('\n')
        actual_list = [actual_list[0]] + actual_list[1].split()
        temporary_list = []
        for i in range(1, len(actual_list), 2):

            temporary_list.append(actual_list[i] + ' ' + actual_list[i+1])
        actual_list = [actual_list[0]] + temporary_list

        assert expected_list == actual_list, \
            "\nExpected list: {0} \nActual list: {1}".format(expected_list, actual_list)

    def test_time_of_delivery(self):
        self.go_to_detailed_info()
        info_time_of_delivery_xpath = "//div[@class = 'time_table clearfix']//tbody//td/span" \
                                      "[@class = 'timearrival-i']/../.."

        time_of_delivery = self.driver.find_elements_by_xpath(info_time_of_delivery_xpath)

        expected_list = ['Час прибуття відправлення', 'З 12:00', 'З 12:00', 'З 12:00', 'З 12:00',
                         'З 12:00', 'З 12:00', 'З 11:50']

        actual_list = []
        for item in time_of_delivery:
            actual_list.append(item.text)

        actual_list = actual_list[0].split('\n')
        actual_list = [actual_list[0]] + actual_list[1].split()
        temporary_list = []
        for i in range(1, len(actual_list), 2):
            temporary_list.append(actual_list[i] + ' ' + actual_list[i + 1])
        actual_list = [actual_list[0]] + temporary_list

        assert expected_list == actual_list, \
            "\nExpected list: {0} \nActual list: {1}".format(expected_list, actual_list)

    def test_money_transfers(self):

        self.driver.find_element_by_id('logo').click()
        money_transfers_xpath = "//a[@class = 'portmone-button']"
        money_transfers = self.driver.find_element_by_xpath(money_transfers_xpath).get_attribute('href')
        self.driver.get(money_transfers)
        actual_transfer_amount = self.driver.find_element_by_id('bill_amount').get_attribute('placeholder')
        expect_transfer_amount = 'від 1 до 25000 грн'
        assert expect_transfer_amount == str(actual_transfer_amount), \
            "\nExpected transfer amount: {0}\nActual transfer amount: {1}".format(
                expect_transfer_amount, actual_transfer_amount)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
