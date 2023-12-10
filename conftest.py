import allure
from selene.support.shared import browser
import pytest


@pytest.fixture()
def open_browser():
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')
    yield
    with allure.step("Закрываем браузер"):
        browser.quit()
