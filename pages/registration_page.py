from selene import browser, have


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

    def choose_dirth_date(self, year, month, day):
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