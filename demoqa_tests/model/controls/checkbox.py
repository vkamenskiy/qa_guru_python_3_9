from selene import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def select(self, *, by_texts: tuple):
        for by_text in by_texts:
            self.element.element_by(have.text(by_text)).click()
        return self
