from HW3.data.users import user_semen
from HW9.pages.simple_registration_page import SimpleRegistrationPage


def test__simple_registration():
    registration_page = SimpleRegistrationPage()
    registration_page.open()
    registration_page.register(user_semen)
    registration_page.should_have_registered(user_semen)
