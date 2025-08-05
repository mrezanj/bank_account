import os, account as acc


def register_account(loged_in: object = None):
    print("\nFILL THE FORM PLEASE ↓ \n")
    user = acc.Account() if not loged_in else loged_in
    os.system("cls")

    while 1:
        try:
            print("\nCHOOSE ACTION : \n")
            print(
                "1 : SHOW BALANCE\n2 : WITHDRAW \n3 : DEPOSITE\n4 : TRANSITION\n5 : SHOW MY INFO\n6 : RENEW EXPIRE DATE\n7 : LOGOUT\n"
            )
            user_2nd_input = input("ENTER HERE PLEASE : ")
            os.system("cls")
            match user_2nd_input:
                case "1":
                    print("CURRENT BALANCE :", user.show_card_balance, "$")
                case "2":
                    withdraw = int(input("HOW MUCH IS WITHDRAW ? "))
                    user.withdraw(amount=withdraw)
                case "3":
                    deposite = int(input("HOW MUCH IS DEPOSITE ? "))
                    user.deposite(amount=deposite)
                case "4":
                    amount = int(input("HOW MUCH IS AMOUNT ? "))
                    contact_card_number = input("PLEASE ENTER CONTACT CARD NUMBER : ")
                    user.transition(amount, contact_card_number)
                case "5":
                    print(f"INFO :\n{user}\n")
                case "6":
                    user.renew_expire_date
                case "7":
                    break
                case default:
                    print("\nENTER VALID NUMBER\n")
            print()
        except Exception as err:
            os.system("cls")
            print(f"ERROR OCCURED | {err}\n")
            continue


def login():
    print("\nWELL BACK\n")
    card_number = input("ENTER YOUR CARD NUMBER PLEASE : ")
    user_password = input("ENTER PASSWORD PLEASE: ")
    user = acc.login(card_number, user_password)
    register_account(loged_in=user)


def forget_password():
    print("\nDON'T WORRY \n")
    card_number = input("ENTER YOUR CARD NUMBER PLEASE : ")
    acc.forget_password(card_number=card_number)


def main():
    os.system("cls")
    print("\nWELCOME TO GITHUB BANK\n")
    while 1:
        try:
            print(
                "1 : CREATE NEW ACCOUNT\n2 : LOGIN TO THE EXISTING ACCOUNT\n3 : FORGET PASSWORD\n4 : EXIT\n"
            )
            user_1st_input = input("SELECT PLEASE : ")
            os.system("cls")
            match user_1st_input:
                case "1":
                    register_account()
                case "2":
                    login()
                case "3":
                    forget_password()
                    os.system("cls")
                    print("\nPASSWORD UPDATED !\n")

                case "4":
                    break
                case default:
                    print("\nENTER VALID NUMBER PLEASE\n")
        except Exception as err:
            os.system("cls")
            print(f"ERROR OCCURED! | {err}\n")
            continue


if __name__ == "__main__":
    main()
    print("GOOD LUCK")
