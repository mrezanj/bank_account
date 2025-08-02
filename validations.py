import re, datetime, bcrypt


def is_valid_name(received_name: str) -> bool:
    return True if len(received_name) >= 3 and received_name.isalpha() else False


def is_valid_age(received_birthDate: datetime.date) -> int | None:

    today = datetime.date.today()
    age = (
        today.year
        - received_birthDate.year
        - (
            (today.month, today.day)
            < (received_birthDate.month, received_birthDate.day)
        )
    )
    return age if 110 >= age >= 18 else None


def is_valid_ssn(received_ssn: str) -> bool:
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    if not re.match(pattern, received_ssn):
        return False
    invalid_prefixes = [str(_).zfill(3) for _ in range(900, 1000)] + ["000", "666"]
    return True if received_ssn.split("-")[0] not in invalid_prefixes else False


def is_valid_email(received_email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, string=received_email) is not None


def is_valid_gender(received_gender: str) -> bool:
    received_gender = received_gender.lower()
    match received_gender:
        case "f":
            return "female"
        case "m":
            return "male"
        case default:
            return None


def is_valid_phone_number(received_phoneNumber: str) -> bool:
    """+1 : USA , CA"""
    # nj said : iKnowThisIsPourCheckDudeSuchAsOtherFunctions :)
    cleaned = re.sub(r"[^\d]", "", string=received_phoneNumber)
    return (cleaned.startswith("1") and len(cleaned) == 11) or len(cleaned) == 10


def is_valid_married(received_isMarried: str) -> bool:
    valid_answers = {"y", "n"}
    received_isMarried = received_isMarried.lower()
    return received_isMarried.lower() in valid_answers


def is_valid_card_number(
    received_card_number: str, valid_accounts: list, self: object
) -> bool:
    # validate correct format
    pattern = r"^\d{4}-\d{4}-\d{4}-\d{3,4}$"
    try:
        received_card_number = re.match(pattern, received_card_number)[0]
    except:
        return False

    digits = [int(d) for d in received_card_number.replace("-", "")]
    sum_check = 0
    parity = len(digits) % 2
    # luhn algorithm
    for ind, digit in enumerate(digits):
        if ind % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum_check += digit
    is_valid = True if not sum_check % 10 else False
    # validate unique item
    is_unique = not (received_card_number in map(lambda x: x[0], valid_accounts))
    if is_valid and is_unique:
        valid_accounts.append((received_card_number, self))
        return True
    return False


def is_valid_card_password(received_password: str) -> bool:
    pattern = r"^\d{4}$"
    return bool(re.match(pattern, received_password)) and received_password[0] != "0"


def secure_password(received_password: str) -> hash:
    pass_bytes, salt = received_password.encode("utf-8"), bcrypt.gensalt()
    return bcrypt.hashpw(pass_bytes, salt)


def check_passwrod(received_password: str, hashed_pass: hash) -> bool:
    pass_bytes = received_password.encode("utf-8")
    return True if bcrypt.checkpw(pass_bytes, hashed_pass) else False


def verifier(action: str):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            args = list(args)
            match action:
                case "get_name":
                    if is_valid_name(args[1]) and is_valid_name(args[2]):
                        args[1], args[2] = args[1].lower(), args[2].lower()
                        func(*args, *kwargs)
                    else:
                        raise ValueError(
                            "NAME & LAST NAME MUST CONTAIN CHARACTERS ONLY | LEN MUST BE 3 OR GREATER"
                        )
                case "get_age":
                    accurate_age = is_valid_age(args[1])
                    if accurate_age is not None:
                        args[1] = accurate_age
                        func(*args, *kwargs)
                    else:
                        raise ValueError("AGE MUST BE BETWEEN 18 AND 110")
                case "get_ssn":
                    if is_valid_ssn(args[1]):
                        func(*args, *kwargs)
                    else:
                        raise ValueError(
                            "SSN FOMAT IS [XXX-XX-XXXX] & PREFIX PART CAN'T BE 000,666 & ANY NUMBER BETWEEN 900 TO 1000"
                        )
                case "get_email":
                    if is_valid_email(args[1]):
                        func(*args, *kwargs)
                    else:
                        raise ValueError("INVALID EMAIL ADDRESS")
                case "get_gender":
                    accurate_gender = is_valid_gender(args[1])
                    if accurate_gender is not None:
                        args[1] = accurate_gender
                        func(*args, **kwargs)
                    else:
                        raise ValueError("ONLY m(MALE) & f(FEMALE) ARE VALID")
                case "get_phone_number":
                    if is_valid_phone_number(args[1]):
                        func(*args, **kwargs)
                    else:
                        raise ValueError(
                            "VALID PHONE NUMBER FORMAT : +(USA CODE)(10 DIGITS)"
                        )
                case "get_is_married":
                    valid_is_married = is_valid_married(args[1])
                    if valid_is_married:
                        args[1] = True if args[1] == "y" else False
                        func(*args, **kwargs)
                    else:
                        raise ValueError("ONLY y(MARRIED) OR n(UNMARRIED)")
                case "get_card_number":
                    if is_valid_card_number(
                        args[1],
                        args[0]._valid_accounts,
                        args[0],
                    ):
                        func(*args, **kwargs)
                    else:
                        raise ValueError(
                            "INVALID CARD NUMBER (VALID FORM : XXXX-XXXX-XXXX-XXX(X)) | IT IS NOT UNIQUE"
                        )
                case "get_card_password":
                    if is_valid_card_password(args[1]):
                        args[1] = secure_password(args[1])
                        func(*args, **kwargs)
                    else:
                        raise ValueError(
                            "PASSWORD MUST BE 4 DIGITS & NOT START WITH '0'"
                        )
                case default:
                    func(*args, **kwargs)

        return wrapper

    return inner_decorator

print("holla")