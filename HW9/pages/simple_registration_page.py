from HW9.pages.registration_page import RegistrationPage


class SimpleRegistrationPage:
    def __init__(self):
        self.page = RegistrationPage()

    def open(self):
        self.page.open_page()

    def register(self, user):
        self.page.fill_name(user.fully_name["name"])
        self.page.fill_lastname(user.fully_name["lastname"])
        self.page.fill_user_email(user.email)
        self.page.choose_gender(user.gender)
        self.page.fill_user_number(user.number)
        self.page.choose_day_birthday(user.birthday)
        self.page.choose_subject(user.subjects)
        self.page.choose_hobby(user.hobbies)
        self.page.load_photo(user.photo_file_name)
        self.page.fill_address(user.current_address)
        self.page.scroll_to_element()
        self.page.select_state(user.state_city["state"])
        self.page.select_city(user.state_city["city"])
        self.page.click_submit()

    def should_have_registered(self, user):
        self.page.should_have_registered(" ".join(user.fully_name.values()),
                                         user.email, user.gender, user.number,
                                         user.birthday.strftime("%d %B,%Y"), ", ".join(user.subjects),
                                         ", ".join(user.hobbies), user.photo_file_name,
                                         user.current_address, " ".join(user.state_city.values()))
