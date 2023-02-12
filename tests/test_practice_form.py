import datetime

from demoqa_tests.model.pages.practice_form import practice_form


def test_successful_submit_student_registration_form():
    (
        practice_form.given_opened()
        .fill_name('Vladislav')
        .fill_last_name('Kamenskiy')
        .fill_email('dje.fry@mail.ru')
        .fill_mobile_number('9162754427')
        .select_date_of_birth(datetime.date(1994, 9, 19))
        .select_subjects('English')
        .select_hobbies('Sports', 'Music')
        .select_picture('test_pictures.webp')
        .fill_current_address('Novotushinskiy proezd 8')
        .select_state('Haryana')
        .select_gender('Male')
        .select_city('Panipat')
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
