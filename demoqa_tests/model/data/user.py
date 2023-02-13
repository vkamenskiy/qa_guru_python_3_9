import datetime

import demoqa_tests


class User:
    def __init__(
        self,
        name,
        last_name,
        email,
        gender,
        mobile_number,
        date_of_birth,
        subjects,
        hobbies,
        picture,
        current_address,
        state,
        city,
    ):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile_number = mobile_number
        self.date_of_birth = date_of_birth
        self.subjects = subjects
        self.hobbies = hobbies
        self.picture = picture
        self.current_address = current_address
        self.state = state
        self.city = city



def format_input_date(value: datetime.date):
    # return value.strftime(demoqa_tests.config.datetime_input_format)
    return value.strftime("%d %b %Y")


def format_view_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_view_format)
