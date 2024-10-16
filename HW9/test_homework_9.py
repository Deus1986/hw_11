from HW3.data.users import user_semen
from HW9.pages.registration_page import RegistrationPage


def test_hw_5():
    registration_page = RegistrationPage()
    registration_page.open_page()
    registration_page.fill_name(user_semen.fully_name["name"])
    registration_page.fill_lastname(user_semen.fully_name["lastname"])
    registration_page.fill_user_email(user_semen.email)
    registration_page.choose_gender(user_semen.gender)
    registration_page.fill_user_number(user_semen.number)
    registration_page.choose_day_birthday(user_semen.birthday)
    registration_page.choose_subject(user_semen.subjects)
    registration_page.choose_hobby(user_semen.hobbies)
    registration_page.load_photo(user_semen.photo_file_name)
    registration_page.fill_address(user_semen.current_address)
    registration_page.scroll_to_element()
    registration_page.select_state(user_semen.state_city["state"])
    registration_page.select_city(user_semen.state_city["city"])
    registration_page.click_submit()
    registration_page.should_have_registered(" ".join(user_semen.fully_name.values()),
                                             user_semen.email, user_semen.gender, user_semen.number,
                                             user_semen.birthday.strftime("%d %B,%Y"), ", ".join(user_semen.subjects),
                                             ", ".join(user_semen.hobbies), user_semen.photo_file_name,
                                             user_semen.current_address, " ".join(user_semen.state_city.values()))
