import os

from selene import browser, have

from pages.registration_page import RegistrationPage
CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "resources")


def test_fill_form(browser_driver):
    registration_page = RegistrationPage()
    registration_page.open_page("/automation-practice-form")
    registration_page.fill_first_name("First")
    registration_page.fill_last_name("Last")
    registration_page.fill_email("qwerty@test.ru")
    registration_page.choose_gender("Female")
    registration_page.fill_number("4567891230")
    registration_page.choose_dirth_date("1990", "6", "14")
    registration_page.choose_subject("h", "Hindi")
    registration_page.choose_subject("m", "Maths")
    registration_page.choose_hobby("Reading")

    browser.element("#uploadPicture").send_keys(os.path.abspath(f"{FILE}/picture.png"))
    browser.element("#currentAddress").type("Any address")
    browser.element("#state").click()
    browser.element("//*[text()='NCR']").click()
    browser.element("#city").click()
    browser.element("//*[text()='Gurgaon']").click()

    browser.element("#submit").click()

    browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text("First Last"))
    browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text("qwerty@test.ru"))
    browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text("Female"))
    browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text("4567891230"))
    browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text("14 July,1990"))
    browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text("Hindi, Maths"))
    browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text("Reading"))
    browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text("picture.png"))
    browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text("Any address"))
    browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text("NCR Gurgaon"))
