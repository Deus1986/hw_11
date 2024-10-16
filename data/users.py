import dataclasses
import datetime
from enum import Enum


class Hobbies(Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


@dataclasses.dataclass
class User:
    fully_name: dict
    email: str
    gender: str
    number: str
    birthday: datetime
    subjects: list[str]
    hobbies: list[Hobbies:str]
    photo_file_name: str
    current_address: str
    state_city: dict


user_semen = User({'name': 'Semen', 'lastname': 'Shpak'}, 'ShpakS@mail.ru', 'Male', '9543231207',
                  datetime.date(1986, 12, 4), ['Chemistry', 'English'],
                  [Hobbies.sports.value, Hobbies.reading.value], 'photo1.jpg',
                  'Ленинградская область, Гатчина, бульвар Авиаторов, 9', {'state': "Haryana", 'city': 'Karnal'})
