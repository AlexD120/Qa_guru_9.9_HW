import allure
from selene import browser, be, by, have
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page("https://github.com")
    search_for_repository("AlexD120/Qa_guru_9.9")
    go_to_repository("AlexD120/Qa_guru_9.9")
    open_issue_tab()
    should_see_issue_with_number("#1", "by AlexD120")
    close_browser()


@allure.step("Открываем главную страницу")
def open_main_page(page):
    browser.open(page)


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number} и содержание текста - by AlexD120")
def should_see_issue_with_number(number, text):
    s(by.partial_text(number)).should(be.visible).should(have.text(text))


@allure.step("Закрываем браузер")
def close_browser():
    browser.close()
