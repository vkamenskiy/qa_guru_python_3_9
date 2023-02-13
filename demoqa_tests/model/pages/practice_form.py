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
        self.name = browser.element("#firstName")
        self.birthday = DatePicker(browser.element("#dateOfBirthInput"))
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender = Radio(browser.all("[name=gender]"))
        self.mobile_number = browser.element("#userNumber")
        self.subjects = Multiselect(browser.element("#subjectsInput"))
        self.hobby = Checkbox(browser.all("[for^=hobbies-checkbox]"))
        self.upload_picture = browser.element("#uploadPicture")
        self.current_address = browser.element("#currentAddress")
        self.state = Dropdown(browser.element("#state"))
        self.city = Dropdown(browser.element("#city"))
        self.submit = browser.element("#submit")
        self.assert_table = browser.element(".table").all("td:nth-of-type(2)")

    def given_opened(self):
        browser.open("/automation-practice-form")
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.5)"'
        )
        ads = browser.all("[id^=google_ads][id$=container__]")
        ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
            command.js.remove
        )

        if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
            ads.perform(command.js.remove)
        return self

    def fill_student(self, user: User):
        self.name.type(user.name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.select(by_text=user.gender)
        self.mobile_number.type(user.mobile_number)
        self.birthday.fill_date(user.date_of_birth)
        self.subjects.select(by_text=user.subjects)
        self.hobby.select(by_texts=user.hobbies)
        self.upload_picture.send_keys(resource.abs_path(user.picture))
        self.current_address.type(user.current_address)
        self.state.select(by_text=user.state)
        self.city.select(by_text=user.city)
        return self

    def submit_form(self):
        self.submit.perform(command.js.click)
        return self

    def assert_submitted(self, user: User):
        self.assert_table.should(
            have.texts(
                user.name + " " + user.last_name,
                user.email,
                user.gender,
                user.mobile_number,
                user.date_of_birth.strftime("%d %B,%Y"),
                user.subjects,
                ', '.join(user.hobbies),
                user.picture,
                user.current_address,
                user.state + " " + user.city,
            )
        )
        return self


practice_form = PracticeForm()
