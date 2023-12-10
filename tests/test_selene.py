from selene import browser, be, by, have
from selene.support.shared.jquery_style import s


def test_selene_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("AlexD120/Qa_guru_9.9").submit()

    s(by.link_text("AlexD120/Qa_guru_9.9")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible).should(have.text("by AlexD120"))
