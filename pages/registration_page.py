import os

from selene import browser, have

from tests.conftest import FILE


class RegistrationPage:
    def open_page(self, page):
        browser.open(page)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def choose_gender(self, gender):
        browser.all("[name='gender']").element_by(have.attribute("value", gender)).element("../label").click()

    def fill_number(self, number):
        browser.element("#userNumber").type(number)

    def choose_birth_date(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{month}']").click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{year}']").click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def choose_subject(self, short_subject, subject):
        browser.element("#subjectsInput").type(short_subject)
        browser.element(".subjects-auto-complete__menu-list").element(f"//*[text()='{subject}']").click()

    def choose_hobby(self, hobby):
        browser.element(f"//label[text()='{hobby}']").click()

    def choose_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"{FILE}/{file_name}"))

    def fill_address(self, address):
        browser.element("#currentAddress").type(address)

    def fill_state(self, state):
        browser.element("#state").click()
        browser.element(f"//*[text()='{state}']").click()

    def fill_city(self, city):
        browser.element("#city").click()
        browser.element(f"//*[text()='{city}']").click()

    def submit(self):
        browser.element("#submit").click()

    def should_have_registered(self, name, email, gender, number, date_birth, subjects, hobbies, picture, address, place):
        browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text(name))
        browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text(email))
        browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text(gender))
        browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text(number))
        browser.element("//table//td[text()='Date of Birth']/../td[2]").should(have.exact_text(date_birth))
        browser.element("//table//td[text()='Subjects']/../td[2]").should(have.exact_text(subjects))
        browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text(hobbies))
        browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text(picture))
        browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text(address))
        browser.element("//table//td[text()='State and City']/../td[2]").should(have.exact_text(place))
