from data.users import user
from pages.registration_page import RegistrationPage


def test_fill_form(browser_driver):
    registration_page = RegistrationPage()
    registration_page.open_page_without_banners("/automation-practice-form")
    registration_page.register_user(user=user)
    registration_page.should_have_registered(user)
