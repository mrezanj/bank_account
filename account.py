import datetime, person
from validations import verifier, check_passwrod


class Account(person.IPerson):
    _valid_accounts = []

    def __init__(self):
        super().__init__()
        self._Account__get_full_info()

    def __get_full_info(self):
        card_num = input("CARD NUMBER [FORMAT : XXXX-XXXX-XXXX-XXX(X)]: ")
        self.get_card_number(card_num)
        card_pass = input("CARD PASSWORD [4 DIGITS] : ")
        self.get_card_password(card_pass)
        self.creation_date = self.renew_date = datetime.date.today()
        self.expire_date = self.creation_date.replace(year=self.creation_date.year + 5)
        self.balance = 100

    @verifier("get_card_number")
    def get_card_number(self, card_number: str) -> None:
        self.card_number = card_number

    @verifier("get_card_password")
    def get_card_password(self, entered_password: str) -> None:
        self.card_password = entered_password

    def check_card_password(self, enterd_password: str) -> bool:
        return True if check_passwrod(enterd_password, self.card_password) else False

    @property
    def check_expire_date(self) -> bool:
        return True if datetime.date.today() < self.expire_date else False

    @property
    def renew_expire_date(self) -> None:
        last_renew = self.renew_date
        self.renew_date = datetime.date.today()
        self.expire_date = self.renew_date.replace(year=self.renew_date.year + 5)
        print(
            f"EXPIRE DATE UPDATED\nNEW EXP DATE : {self.expire_date}\nLAST RENEW DATE : {last_renew}\nCREATION DATE : {self.creation_date}"
        )

    @property
    def show_card_balance(self) -> int | ValueError:
        if self.check_expire_date:
            return self.balance
        raise ValueError("card is expired | password's incorrect")

    def withdraw(self, amount: int) -> None | ValueError:
        if amount <= self.show_card_balance:
            self.balance -= amount
            print(f"WITHDRAW APPLIED\nNEW BALANCE : {self.balance} $")
        else:
            raise ValueError("YOU DO NOT HAVE THIS AMOUNT OF MONEY IN YOUR ACCOUNT")

    def deposite(self, amount: int) -> None | ValueError:
        if amount > 0:
            self.balance += amount
            print(f"WITHDRAW APPLIED\nNEW BALANCE : {self.balance} $")
        else:
            raise ValueError("ENTER POSITIVE VALUE PLEASE")

    def transition(self, amount: int, card_number: str) -> None | ValueError:
        while 1:
            needs_change = False
            if amount <= self.show_card_balance:
                receiver = None
                for card_num, user_obj in Account._valid_accounts:
                    if card_number == card_num:
                        receiver = user_obj
                        break
                if receiver and card_number != self.card_number:
                    print(
                        f"CHECK UP!\n{amount}$ TO {receiver.name} {receiver.last_name} ACCOUNT ? [ONLY PRESS ENTER TO CONFIRM] : ",
                        end=" ",
                    )
                    user_input = input()
                    needs_change = True if user_input else False
                    if not needs_change:
                        self.balance -= amount
                        receiver.balance += amount
                        print(
                            f"""\nTRANSITIONED SUCCESSFULLY!\nAMOUNT : {amount}$\nSENDER CARD : {self.card_number}\nRECEIVER CARD : {receiver.card_number}\nDATE : {datetime.date.today()}\nNEW BALANCE : {self.balance}$\n"""
                        )
                        break
                    else:
                        card_number = input("enter new card number : ")
                        amount = int(input("enter new amount : "))

                else:
                    raise ValueError("INVAILD CARD NUMBER")
            else:
                raise ValueError("YOU DO NOT HAVE THIS AMOUNT OF MONEY IN YOUR ACCOUNT")

    def __str__(self):
        return f"""FULL NAME : {self.name} {self.last_name}\nEMAIL : {self.email}\nPHONE NUMBER : {self.phone_number}\nGENDER : {self.gender}\nAGE : {self.age}\nSSN : {self.ssn}\nis married ? {self.is_married}\nCARD NUMBER : {self.card_number}"""


def login(card_number: str, password: str) -> object:
    found_account = list(
        (filter(lambda person: person[0] == card_number, Account._valid_accounts))
    )
    if found_account:
        found_account = found_account[0][1]
    if found_account:
        if found_account.check_card_password(password):
            return found_account
        else:
            raise ValueError("INCORRECT PASSWORD")
    else:
        raise ValueError("NO ACCOUNT FOUND WITH THIS CARD NUMBER")


def forget_password(card_number: str) -> None:
    found_account = list(
        (filter(lambda person: person[0] == card_number, Account._valid_accounts))
    )
    if found_account:
        found_account = found_account[0][1]
    if found_account:
        ssn = input("SOCIAL_SECURITY_NUMBER [FORMAT : DDD-DD-DDDD] : ")
        if ssn == found_account.ssn:
            phone_number = input("PHONE NUMBER [.E.G : +1(OPTIONAL) (DDD)-DDDD-DDD] : ")
            if phone_number == found_account.phone_number:
                new_password = input("ENTER YOUR NEW PASSWORD : ")
                found_account.get_card_password(new_password)
            else:
                raise ValueError("INVALID PHONE NUMBER")
        else:
            raise ValueError("INVALIE SSN")
    else:
        raise ValueError("NO ACCOUNT FOUND WITH THIS CARD NUMBER")
