import datetime

from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.multiselect import Multiselect
from demoqa_tests.model.controls.radio import Radio
from demoqa_tests.utils import resource


class PracticeForm:
    def __init__(self):
        self.name = browser.element('#firstName')
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = Radio(browser.all('[name=gender]'))
        self.mobile_number = browser.element('#userNumber')
        self.subjects = Multiselect(browser.element('#subjectsInput'))
        self.hobby = Checkbox(browser.all('[for^=hobbies-checkbox]'))
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = Dropdown(browser.element('#state'))
        self.city = Dropdown(browser.element('#city'))
        self.submit = browser.element('#submit')

    def given_opened(self):
        browser.open('/automation-practice-form')
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.5)"'
        )
        ads = browser.all('[id^=google_ads][id$=container__]')
        ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
            command.js.remove
        )

        if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
            ads.perform(command.js.remove)
        return self

    def fill_name(self, value: str):
        self.name.type(value)
        return self

    def fill_last_name(self, value: str):
        self.last_name.type(value)
        return self

    def fill_email(self, value: str):
        self.email.type(value)
        return self

    def select_gender(self, value: str):
        self.gender.select(by_text=value)
        return self

    def fill_mobile_number(self, value: str):
        self.mobile_number.type(value)
        return self

    def select_date_of_birth(self, value: datetime.date):
        self.birthday.fill_date(value)
        return self

    def select_subjects(self, value: str):
        self.subjects.select(by_text=value)
        return self

    def select_hobbies(self, *texts: str):
        self.hobby.select(by_texts=texts)
        return self

    def select_picture(self, file: str):
        self.upload_picture.send_keys(resource.abs_path(file))
        return self

    def fill_current_address(self, value: str):
        self.current_address.type(value)
        return self

    def select_state(self, value: str):
        self.state.select(by_text=value)
        return self

    def select_city(self, value: str):
        self.city.select(by_text=value)
        return self

    def submit_form(self):
        self.submit.perform(command.js.click)
        return self

    def assert_submitted(self, *data):
        browser.element('.table').all('td:nth-of-type(2)').should(have.texts(data))
        return self


practice_form = PracticeForm()
