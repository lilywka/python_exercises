from selenium import webdriver
import unittest


class StorageXpath:

    service_types_xpath = "//input[@id = 'EstimateDateForm_ServiceType']/../ins"
    address_address_xpath = "//ul[@class = 'list drop-down-ul hover_list' or @class = 'list drop-down-ul']" \
                            "//li[@data-value = 'DoorsDoors']"
    address_department_xpath = "//ul[@class = 'list drop-down-ul hover_list' " \
                               "or @class = 'list drop-down-ul']//li[@data-value = 'DoorsWarehouse']"
    department_department_xpath = "//ul[@class = 'list drop-down-ul hover_list'" \
                                  " or @class = 'list drop-down-ul']//li[@data-value = 'WarehouseWarehouse']"
    department_address_xpath = "//ul[@class = 'list drop-down-ul hover_list'" \
                               " or @class = 'list drop-down-ul']//li[@data-value = 'WarehouseDoors']"
    sender_city_kiev_xpath = "//input[@id = 'EstimateDateForm_senderCity']" \
                             "/../..//li[@data-value = '8d5a980d-391c-11dd-90d9-001a92567626']"
    recipient_city_odessa_xpath = "//input[@id = 'EstimateDateForm_recipientCity']" \
                                  "/../..//li[@data-value = 'db5c88d0-391c-11dd-90d9-001a92567626']"
    button_calculate_date = "//input[@name = 'yt0']"
    delivery_date_xpath = "//div[@class = 'highlight']/b"


class CorrectInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://novaposhta.ua/onlineorder/estimatedate')
        cls.storage_xpath = StorageXpath()

    def setUp(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_address_address(self):

        service_types = self.driver.find_element_by_xpath(self.storage_xpath.service_types_xpath)
        address_address = self.driver.find_element_by_xpath(self.storage_xpath.address_address_xpath)

        service_types.click()
        address_address.click()

        sender_city = self.driver.find_element_by_id('EstimateDateForm_senderCity')
        sender_city_kiev = self.driver.find_element_by_xpath(self.storage_xpath.sender_city_kiev_xpath)
        sender_city.send_keys('Київ')
        sender_city_kiev.click()

        resipient_city = self.driver.find_element_by_id('EstimateDateForm_recipientCity')
        recipient_city_odessa = self.driver.find_element_by_xpath(self.storage_xpath.recipient_city_odessa_xpath)
        resipient_city.send_keys('Одеса')
        recipient_city_odessa.click()

        calculate_date = self.driver.find_element_by_xpath(self.storage_xpath.button_calculate_date)
        calculate_date.click()

        delivery_date = self.driver.find_element_by_xpath(self.storage_xpath.delivery_date_xpath)
        actual_delivery_date = delivery_date.text
        expected_delivery_date = '22 квітня 2019'
        assert expected_delivery_date == actual_delivery_date, "\nExpected delivery date: {0}\nActual delivery date:{1}"\
                                                               .format(expected_delivery_date, actual_delivery_date)

    def test_address_department(self):
        service_types = self.driver.find_element_by_xpath(self.storage_xpath.service_types_xpath)
        address_department = self.driver.find_element_by_xpath(self.storage_xpath.address_department_xpath)
        service_types.click()
        address_department.click()

        calculate_date = self.driver.find_element_by_xpath(self.storage_xpath.button_calculate_date)
        calculate_date.click()

        delivery_date = self.driver.find_element_by_xpath(self.storage_xpath.delivery_date_xpath)
        actual_delivery_date = delivery_date.text
        expected_delivery_date = '22 квітня 2019'
        assert expected_delivery_date == actual_delivery_date, "\nExpected delivery date: {0}\nActual delivery date:{1}"\
                                                               .format(expected_delivery_date, actual_delivery_date)

    def test_department_department(self):
        service_types = self.driver.find_element_by_xpath(self.storage_xpath.service_types_xpath)
        department_department = self.driver.find_element_by_xpath(self.storage_xpath.department_department_xpath)
        service_types.click()
        department_department.click()

        calculate_date = self.driver.find_element_by_xpath(self.storage_xpath.button_calculate_date)
        calculate_date.click()

        delivery_date = self.driver.find_element_by_xpath(self.storage_xpath.delivery_date_xpath)
        actual_delivery_date = delivery_date.text
        expected_delivery_date = '22 квітня 2019'
        assert expected_delivery_date == actual_delivery_date, "\nExpected delivery date: {0}\nActual delivery date:{1}"\
                                                               .format(expected_delivery_date, actual_delivery_date)

    def test_department_address(self):
        service_types = self.driver.find_element_by_xpath(self.storage_xpath.service_types_xpath)
        department_address = self.driver.find_element_by_xpath(self.storage_xpath.department_address_xpath)
        service_types.click()
        department_address.click()

        calculate_date = self.driver.find_element_by_xpath(self.storage_xpath.button_calculate_date)
        calculate_date.click()

        delivery_date = self.driver.find_element_by_xpath(self.storage_xpath.delivery_date_xpath)
        actual_delivery_date = delivery_date.text
        expected_delivery_date = '22 квітня 2019'
        assert expected_delivery_date == actual_delivery_date, "\nExpected delivery date: {0}\nActual delivery date:{1}" \
                                                               .format(expected_delivery_date, actual_delivery_date)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
