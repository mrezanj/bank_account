import datetime
from validations import verifier


class IPerson:
    def __init__(self):
        self._IPerson__get_full_info()

    def __get_full_info(self):
        name, l_name = input(
            "NAME AND LAST NAME WITH SPACE BETWEEN [.E.G JOHN WICK]: "
        ).split(" ")
        self.get_full_name(name, l_name)
        birth_date = tuple(
            map(
                int,
                input(
                    "enter your birth date and put space between like {year month day}: "
                ).split(),
            )
        )
        birth_date = datetime.date(birth_date[0], birth_date[1], birth_date[2])
        self.get_age(birth_date)
        ssn = input("SOCIAL_SECURITY_NUMBER [FORMAT : DDD-DD-DDDD] : ")
        self.get_ssn(ssn)
        email = input("EMAIL : ")
        self.get_email(email)
        gender = input("GENDER [m or f] : ")
        self.get_gender(gender)
        phone_number = input("PHONE NUMBER [.E.G : +1(OPTIONAL) (DDD)-DDDD-DDD] : ")
        self.get_phone_number(phone_number)
        is_married = input("MARRIED ? [y or n] : ")
        self.get_is_married(is_married)

    @verifier("get_name")
    def get_full_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name

    @verifier("get_age")
    def get_age(self, birth_date: datetime.date) -> None:
        self.age = birth_date

    @verifier("get_ssn")
    def get_ssn(self, ssn: str) -> None:
        self.ssn = ssn

    @verifier("get_email")
    def get_email(self, email: str) -> None:
        self.email = email

    @verifier("get_gender")
    def get_gender(self, gender: str) -> None:
        self.gender = gender

    @verifier("get_phone_number")
    def get_phone_number(self, phone_number: str) -> None:
        self.phone_number = phone_number

    @verifier("get_is_married")
    def get_is_married(self, is_married: str) -> None:
        self.is_married = is_married

    @property
    def show_full_info(self) -> str:
        text = f"\nfull name : {self.name+' '+self.last_name}\nage : {self.age}\ngender : {self.gender}\nsocial security number : {self.ssn}\nemail : {self.email}\nphone number : {self.phone_number}\nmarried : {self.is_married}"
        return text

    def __str__(self):
        return f"\n{self.name} {self.last_name} - {self.age} years old"
