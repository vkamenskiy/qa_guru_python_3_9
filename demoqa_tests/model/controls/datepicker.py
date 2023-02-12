import datetime
import sys

from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys


# class DatePicker:
#
#     def __init__(self, element):
#         self.element = element
#
#     def fill_date(self, date: datetime.date):
#         day = date.strftime('%d')
#         month = int(date.strftime('%-m')) - 1
#         year = date.strftime('%Y')
#         self.element.click()
#         browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
#         browser.element(f'.react-datepicker__month-select [value="{str(month)}"]').click()
#         browser.element(f'.react-datepicker__day--0{day}').click()
#         return self


class DatePicker:

    def __init__(self, element):
        self.element = element

    def fill_date(self, date: datetime.date):
        self.element.click()
        browser.element(f'.react-datepicker__year-select [value="{date.year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{date.month - 1}"]').click()
        browser.element(f'.react-datepicker__day--0{date.day}').click()
        return self


# в этом варианте не всегда стаибльно работает вставка даты
# иногда он не стирает дефолтную дату и лепит на нее сверху новую
# возможно можно решить какими-то костылями с таймаутами

# class DatePicker:
#
#     def __init__(self, element):
#         self.element = element
#
#     def set_date(self, date: datetime.date):
#         modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
#         self.element.send_keys(
#             modifier_key + 'a' + Keys.NULL,
#             date.strftime('%d %b %Y')
#         ).press_enter()
#         return self
