import datetime

from demoqa_tests.model.pages.practice_form import practice_form
from demoqa_tests.model.data.user import User


def test_successful_submit_student_registration_form():
    (
        practice_form.given_opened()
        .fill_name(Vlad)
        .fill_last_name(Vlad)
        .fill_email(Vlad)
        .fill_mobile_number(Vlad)
        .select_date_of_birth(Vlad)
        .select_subjects(Vlad)
        .select_hobbies(Vlad)
        .select_picture(Vlad)
        .fill_current_address(Vlad)
        .select_state(Vlad)
        .select_gender(Vlad)
        .select_city(Vlad)
        .submit_form()
    )

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
    "Vladislav",
    "Kamenskiy",
    "dje.fry@mail.ru",
    "Male",
    "9162754427",
    datetime.date(1994, 9, 19),
    "English",
    ("Sports", "Music"),
    "test_pictures.webp",
    "Novotushinskiy proezd 8",
    "Haryana",
    "Panipat",
)
