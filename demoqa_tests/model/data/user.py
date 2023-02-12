import datetime

import demoqa_tests


def format_input_date(value: datetime.date):
    #return value.strftime(demoqa_tests.config.datetime_input_format)
    return value.strftime('%d %b %Y')


def format_view_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_view_format)
