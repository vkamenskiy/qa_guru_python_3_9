from selene import have
from selene.support.shared import browser


class Multiselect:
    def __init__(self, element):
        self.element = element

    def select(self, by_text: str):
        self.element.type(f'{by_text[:2]}')
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(by_text)
        ).click()
        return self
