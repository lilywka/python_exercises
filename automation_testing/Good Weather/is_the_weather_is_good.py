from selenium import webdriver
import datetime
from calendar import monthrange

driver = webdriver.Chrome()
driver.get('https://www.gismeteo.ua/ua/weather-odessa-4982/month/')

weather_xpath = "//img[@src = '//s1.gismeteo.ua/static/images/icons/new/d.sun.png']/../../span"

weather = driver.find_elements_by_xpath(weather_xpath)
driver.execute_script("window.scrollTo(0,300)")

sunny_date = []
for i in weather:
    sunny_date.append(i.text)
print(sunny_date)
driver.close()

i = datetime.datetime.now()
month_range = monthrange(i.year, i.month)

first_day = i.day
last_day = first_day + 30 - month_range[1]
q = False
while not q:
    print('Enter day of month')
    try:
        date = int(input())
    except ValueError:
        print('Please input a valid integer')
        continue

    if first_day <= date <= month_range[1] or month_range[0] <= date < last_day:
        if str(date) in sunny_date:
            print('This day is sunny!!')
        else:
            print('This day is not sunny!!')
    else:
        print('The day is out of range. Enter day from {0} of current month to {1} of next month'.format(first_day, last_day - 1))

    print('Do you want to quit(y/n)?')
    choice = input()
    q = choice != 'n'
