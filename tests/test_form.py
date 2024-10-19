from pages.registration_page import RegistrationPage


def test_fill_form(browser_driver):
    registration_page = RegistrationPage()
    registration_page.open_page("/automation-practice-form")
    registration_page.fill_first_name("First")
    registration_page.fill_last_name("Last")
    registration_page.fill_email("qwerty@test.ru")
    registration_page.choose_gender("Female")
    registration_page.fill_number("4567891230")
    registration_page.choose_birth_date("1990", "6", "14")
    registration_page.choose_subject("h", "Hindi")
    registration_page.choose_subject("m", "Maths")
    registration_page.choose_hobby("Reading")
    registration_page.choose_picture("picture.png")
    registration_page.fill_address("Any address")
    registration_page.fill_state("NCR")
    registration_page.fill_city("Gurgaon")
    registration_page.submit()
    registration_page.should_have_registered("First Last",
                                             "qwerty@test.ru",
                                             "Female",
                                             "4567891230",
                                             "14 July,1990",
                                             "Hindi, Maths",
                                             "Reading",
                                             "picture.png",
                                             "Any address",
                                             "NCR Gurgaon")
