import datetime

from demoqa_tests.model.pages.practice_form import practice_form
from demoqa_tests.model.data.user import User


def test_successful_submit_student_registration_form():
    practice_form.given_opened()

    practice_form.fill_student(Vlad).submit_form()

    practice_form.assert_submitted(
        'Vladislav Kamenskiy',
        'dje.fry@mail.ru',
        'Male',
        '9162754427',
        datetime.date(1994, 9, 19).strftime('%d %B,%Y'),
        'English',
        'Sports, Music',
        'test_pictures.webp',
        'Novotushinskiy proezd 8',
        'Haryana Panipat'
    )


Vlad = User(
    name="Vladislav",
    last_name="Kamenskiy",
    email="dje.fry@mail.ru",
    gender="Male",
    mobile_number="9162754427",
    date_of_birth=datetime.date(1994, 9, 19),
    subjects="English",
    hobbies=("Sports", "Music"),
    picture="test_pictures.webp",
    current_address="Novotushinskiy proezd 8",
    state="Haryana",
    city="Panipat",
)
