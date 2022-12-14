from selene.support.shared import browser
from selene import be, have

def test_google_search_positive(open_browser):

    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))

def test_google_search_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('CSKA').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene:'))