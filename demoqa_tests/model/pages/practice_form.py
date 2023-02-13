from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.multiselect import Multiselect
from demoqa_tests.model.controls.radio import Radio
from demoqa_tests.model.data.user import User
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

    def fill_name(self, user: User):
        self.name.type(user.name)
        return self

    def fill_last_name(self, user: User):
        self.last_name.type(user.last_name)
        return self

    def fill_email(self, user: User):
        self.email.type(user.email)
        return self

    def select_gender(self, user: User):
        self.gender.select(by_text=user.gender)
        return self

    def fill_mobile_number(self, user: User):
        self.mobile_number.type(user.mobile_number)
        return self

    def select_date_of_birth(self, user: User):
        self.birthday.fill_date(user.date_of_birth)
        return self

    def select_subjects(self, user: User):
        self.subjects.select(by_text=user.subjects)
        return self

    def select_hobbies(self, user: User):
        self.hobby.select(by_texts=user.hobbies)
        return self

    def select_picture(self, user: User):
        self.upload_picture.send_keys(resource.abs_path(user.picture))
        return self

    def fill_current_address(self, user: User):
        self.current_address.type(user.current_address)
        return self

    def select_state(self, user: User):
        self.state.select(by_text=user.state)
        return self

    def select_city(self, user: User):
        self.city.select(by_text=user.city)
        return self

    def submit_form(self):
        self.submit.perform(command.js.click)
        return self

    def assert_submitted(self, *data):
        browser.element('.table').all('td:nth-of-type(2)').should(have.texts(data))
        return self


practice_form = PracticeForm()
