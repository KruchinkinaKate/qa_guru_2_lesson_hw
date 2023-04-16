import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def browser_open():
    browser.open('https://www.google.com/')
    browser.driver.set_window_size(1080, 1080)


def test_successful(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_unsuccessful(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ffffffgggggggggbbfdg').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

