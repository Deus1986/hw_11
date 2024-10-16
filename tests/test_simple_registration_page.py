from data.users import user_semen
from pages.simple_registration_page import SimpleRegistrationPage


def test_simple_registration():
    registration_page = SimpleRegistrationPage()
    registration_page.open()
    registration_page.register(user_semen)
    registration_page.should_have_registered(user_semen)
