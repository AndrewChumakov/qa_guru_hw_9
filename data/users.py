import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    birthday_date: dict[str, str]
    subject: list[str]
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(
    first_name="First",
    last_name="Last",
    email="qwerty@test.ru",
    gender="Female",
    number="4567891230",
    birthday_date={"month_number": "6", "month": "July", "year": "1990", "day": "04"},
    subject=["Hindi", "Maths"],
    hobby="Reading",
    picture="picture.png",
    address="Any address",
    state="NCR",
    city="Gurgaon"
)
