from selenium import webdriver
import unittest
import requests


# 2) Create a Python script (no need to use unittests) that reads the weather from Darksy API

url = 'https://api.darksky.net/forecast/561c7b438d1968d624c03ba3e1293751/46.469391,30.740883/?si=sl'

r = requests.get(url=url)

init_dict = r.json()

correct_names_dict = {'summary': 'The weather in Odessa',
                      'temperature': 'Temperature',
                      'humidity': 'Humidity',
                      'windSpeed': 'Wind speed',
                      'windGust': 'Wind guest'}

result_dict = {}

for key, val in init_dict['currently'].items():
    if key in correct_names_dict:
        new_key = correct_names_dict[key]
        result_dict[new_key] = val

with open('dict.txt', 'w') as i:
    for k, v in result_dict.items():
        i.write('{}:{}\n'.format(k, v))
print(result_dict)

# 1) Create a test class that has two tests: NP tracking using UI and NP tracking API (requests)


class NovaPoshtaTracking(unittest.TestCase):

    def test_np_tracking(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://novaposhta.ua')
        self.driver.find_element_by_id('cargo_number').send_keys('20400048799001\n')
        actual_result = (self.driver.find_element_by_xpath("//div[@class = 'not-found']/span")).text
        expected_result = 'Експрес-накладної з таким номером не знайдено.'
        assert expected_result == actual_result, "\nExpected result: {0}\nActual result:{1}" \
            .format(expected_result, actual_result)
        self.driver.close()

    def test_api_np_tracking(self):

        api_key = '541c88dc7acf85d465acbc0460fcc5eb'

        request_body = {
                "apiKey": api_key,
                "modelName": "TrackingDocument",
                "calledMethod": "getStatusDocuments",
                "methodProperties": {
                    "Documents": [
                        {
                            "DocumentNumber": "20400048799001",
                            "Phone": ""
                        }
                    ]
                }
            }

        r = requests.post('https://api.novaposhta.ua/v2.0/json/', json=request_body)
        np_tracking = r.json()
        assert r.status_code == 200, 'status code is not 200'
        # expected_np_tracking = r.json()['data'][2]
        # print(expected_np_tracking)
        actual_np_tracking = {}
        expected_np_tracking = {'Status': 'Номер не знайдено'}
        for key, val in np_tracking['data'][0].items():
            if key in expected_np_tracking:
                actual_np_tracking[key] = val
        assert expected_np_tracking == actual_np_tracking, "\nExpected tracking: {0}\nActual tracking:{1}" \
            .format(expected_np_tracking, actual_np_tracking)


if __name__ == '__main__':
    unittest.main()
