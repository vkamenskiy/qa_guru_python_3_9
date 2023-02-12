from selene import command, have
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element):
        self.element = element

    def select(self, by_text: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(by_text)
        ).perform(command.js.click)
        return self
