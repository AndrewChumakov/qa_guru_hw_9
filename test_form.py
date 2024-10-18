import os

from selene import browser, have


def test_fill_form(browser_driver):
    browser.open("/automation-practice-form")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element("#firstName").type("First")
    browser.element("#lastName").type("Last")
    browser.element("#userEmail").type("qwerty@test.ru")
    # browser.element("[for='gender-radio-2']").click()
    browser.all('[name="gender"]').element_by(have.attribute('value', 'Female')).element('../label').click()
    browser.element("#userNumber").type("4567891230")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element("[value='6']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element("[value='1990']").click()
    browser.element(".react-datepicker__day--014").click()
    browser.element("#subjectsInput").type("h")
    browser.element(".subjects-auto-complete__menu-list").element('//*[text()="Hindi"]').click()
    browser.element("#subjectsInput").type("m")
    browser.element(".subjects-auto-complete__menu-list").element('//*[text()="Maths"]').click()
    # browser.element("[for='hobbies-checkbox-2']").click()
    browser.element('//label[text()="Reading"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("picture.png"))
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
