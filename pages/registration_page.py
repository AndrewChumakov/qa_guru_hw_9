import os

from selene import browser, have

from data.users import User
from tests.conftest import FILE


class RegistrationPage:
    def open_page(self, page):
        browser.open(page)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def _fill_first_name(self, first_name):
        browser.element("#firstName").type(first_name)

    def _fill_last_name(self, last_name):
        browser.element("#lastName").type(last_name)

    def _fill_email(self, email):
        browser.element("#userEmail").type(email)

    def _choose_gender(self, gender):
        browser.all("[name='gender']").element_by(have.attribute("value", gender)).element("../label").click()

    def _fill_number(self, number):
        browser.element("#userNumber").type(number)

    def _choose_birth_date(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f"[value='{month}']").click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f"[value='{year}']").click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def _choose_subject(self, short_subject, subject):
        browser.element("#subjectsInput").type(short_subject)
        browser.element(".subjects-auto-complete__menu-list").element(f"//*[text()='{subject}']").click()

    def _choose_hobby(self, hobby):
        browser.element(f"//label[text()='{hobby}']").click()

    def _choose_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(os.path.abspath(f"{FILE}/{file_name}"))

    def _fill_address(self, address):
        browser.element("#currentAddress").type(address)

    def _fill_state(self, state):
        browser.element("#state").click()
        browser.element(f"//*[text()='{state}']").click()

    def _fill_city(self, city):
        browser.element("#city").click()
        browser.element(f"//*[text()='{city}']").click()

    def _submit(self):
        browser.element("#submit").click()

    def register_user(self, user: User):
        self._fill_first_name(user.first_name)
        self._fill_last_name(user.last_name)
        self._fill_email(user.email)
        self._choose_gender(user.gender)
        self._fill_number(user.number)
        self._choose_birth_date(user.birthday_date["year"], user.birthday_date["month_number"],
                                user.birthday_date["day"])
        for subject in user.subject:
            self._choose_subject(subject[0], subject)
        self._choose_hobby(user.hobby)
        self._choose_picture(user.picture)
        self._fill_address(user.address)
        self._fill_state(user.state)
        self._fill_city(user.city)
        self._submit()

    def should_have_registered(self, user):
        browser.element("//table//td[text()='Student Name']/../td[2]").should(have.exact_text(user.first_name + " " +
                                                                                              user.last_name))
        browser.element("//table//td[text()='Student Email']/../td[2]").should(have.exact_text(user.email))
        browser.element("//table//td[text()='Gender']/../td[2]").should(have.exact_text(user.gender))
        browser.element("//table//td[text()='Mobile']/../td[2]").should(have.exact_text(user.number))
        (browser.element("//table//td[text()='Date of Birth']/../td[2]").
         should(have.exact_text(user.birthday_date["day"]
                                + " " + user.birthday_date["month"] + "," + user.birthday_date["year"])))
        (browser.element("//table//td[text()='Subjects']/../td[2]").
         should(have.exact_text(", ".join(subject for subject in user.subject))))
        browser.element("//table//td[text()='Hobbies']/../td[2]").should(have.exact_text(user.hobby))
        browser.element("//table//td[text()='Picture']/../td[2]").should(have.exact_text(user.picture))
        browser.element("//table//td[text()='Address']/../td[2]").should(have.exact_text(user.address))
        (browser.element("//table//td[text()='State and City']/../td[2]").
         should(have.exact_text(user.state + " " + user.city)))