import os
import time
from termcolor import colored

import validators as VALIDATORS
import queries as QUERIES

from classes.session import session
from classes import computer, drinks

import classes.admin as ADMIN

comp = computer.computer()
drink = drinks.drinks()


# login
#   member
#   admin
#     Master entry
#         member entry
#             Add New Member
#             Show Member
#             Update Record
#             Delete Record
#             Search Record
#             Return
#         computer entry
#             Add New Computer
#             Show Computer
#             Update Record
#             Delete Record
#             Search Record
#             Return
#     Return
#     Café management
#         Booking
#             Member Login
#             Member Log Out
#             Non-Member User Log in
#             Non Member User Log Out
#             Return
#         Charges
#             Take charges
#             Show Charges
#             Return
#         Booking
#             Add New Drink
#             Show Drinks
#             Update Record
#             Delete Record
#             Search Record
#             Return
#     Return
# create account
# Exit


def main():
    print("\n\nWelcome to cybercafe management system\n\n")
    print("1. Admin login")
    print("2. Terminate Progrm")
    main_input = VALIDATORS.get_numeric("\n> ", 1, 2)

    while main_input != 2:
        if main_input == 1:
            user_input2 = None
            while user_input2 != 2:
                os.system("clear")
                user_name = VALIDATORS.get_user_name("Enter your user name: ")
                password = VALIDATORS.get_password("Enter your password: ")
                user_attributes = QUERIES.lookup_item("databases/users.json", user_name)
                while user_attributes == None:
                    print(
                        colored(
                            "\nUSER DOES NOT EXIST EXCEPTION: user '{}' does not exist in '{}' database".format(
                                user_name, "databases/users.json"
                            ),
                            "red",
                        )
                    )
                    print("\nChoose an option to continue:")
                    print("1. try to login again")
                    print("2. return")
                    option = VALIDATORS.get_numeric("> ", 1, 2)
                    if option == 1:
                        os.system("clear")
                        user_name = VALIDATORS.get_user_name("Enter your user name: ")
                        password = VALIDATORS.get_password("Enter your password: ")
                        user_attributes = QUERIES.lookup_item(
                            "databases/users.json", user_name
                        )
                    elif option == 2:
                        # Terminate Progrm option
                        break
                if user_attributes != None:
                    stored_password = QUERIES.get_attribute(
                        "databases/users.json", user_name, "password"
                    )
                    if stored_password != password:
                        print(
                            colored(
                                "\nINVALID PASSWORD EXCEPTION: you have written a wrong password, try again!",
                                "red",
                            )
                        )
                        time.sleep(4)
                        continue
                    elif stored_password == password:
                        role = user_attributes.get("role")
                        if role == "admin":
                            first_name = user_attributes.get("first_name")
                            last_name = user_attributes.get("last_name")
                            print(
                                colored(
                                    "\nSUCCESS: you have logged in to the system as {} {}".format(
                                        first_name, last_name
                                    ),
                                    "green",
                                )
                            )
                            time.sleep(5)

                            admin_attributes = QUERIES.lookup_item(
                                "databases/users.json", user_name
                            )
                            admin_object = ADMIN.construct_object(admin_attributes)
                            os.system("clear")
                            print(
                                "\n\nWelcome to cybercafe management system admin dashboard\n\n"
                            )
                            print("1. master entry")
                            print("2. cafe management")
                            print("3. admin logout")
                            admin_input = VALIDATORS.get_numeric("\n> ", 1, 3)

                            while admin_input != 3:
                                if admin_input == 1:
                                    master_entry_input = None
                                    # master entry options starts here
                                    while master_entry_input != 4:
                                        os.system("clear")
                                        print("1. member entry")
                                        print("2. computer entry")
                                        print("3. session entry")
                                        print("4. return")
                                        master_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 4
                                        )
                                        if master_entry_input == 1:
                                            member_entry_input = None
                                            while member_entry_input != 6:
                                                os.system("clear")
                                                print("1. Add New Member")
                                                print("2. Show Member")
                                                print("3. Update Record")
                                                print("4. Delete Record")
                                                print("5. Search Record")
                                                print("6. Return")
                                                member_entry_input = (
                                                    VALIDATORS.get_numeric("\n> ", 1, 6)
                                                )
                                                if member_entry_input == 1:
                                                    # 1. Add New Member
                                                    os.system("clear")
                                                    admin_object.add_new_member()
                                                elif member_entry_input == 2:
                                                    # 2. Show Member
                                                    while True:
                                                        os.system("clear")
                                                        member_user_name = (
                                                            VALIDATORS.get_user_name(
                                                                "Enter user name: "
                                                            )
                                                        )
                                                        admin_object.show_member(
                                                            member_user_name
                                                        )
                                                        show_member_option_input = VALIDATORS.get_numeric(
                                                            "\n\nChoose an option to continue: \n1. show another user\n2. return\nYour input is: ",
                                                            1,
                                                            2,
                                                        )
                                                        if (
                                                            show_member_option_input
                                                            == 2
                                                        ):
                                                            break

                                                elif member_entry_input == 3:
                                                    # 3. Update Record
                                                    while True:
                                                        os.system("clear")
                                                        member_user_name = (
                                                            VALIDATORS.get_user_name(
                                                                "Enter user name: "
                                                            )
                                                        )
                                                        member_key = input(
                                                            "Enter attribute name: "
                                                        )
                                                        member_value = input(
                                                            "Enter new value of {}: ".format(
                                                                member_key
                                                            )
                                                        )

                                                        admin_object.update_record(
                                                            member_user_name,
                                                            member_key,
                                                            member_value,
                                                        )

                                                        print(
                                                            "\n{} attributes after updating are: \n".format(
                                                                member_user_name
                                                            )
                                                        )
                                                        admin_object.show_member(
                                                            member_user_name
                                                        )
                                                        update_member_option_input = VALIDATORS.get_numeric(
                                                            "\n\nChoose an option to continue: \n1. update attribute of another user\n2. return\nYour input is: ",
                                                            1,
                                                            2,
                                                        )
                                                        if (
                                                            update_member_option_input
                                                            == 2
                                                        ):
                                                            break
                                                elif member_entry_input == 4:
                                                    # 4. Delete Record
                                                    pass
                                                elif member_entry_input == 5:
                                                    # 5. Search Record
                                                    pass
                                        elif master_entry_input == 2:
                                            computer_entry_input = None
                                            while computer_entry_input != 6:
                                                os.system("clear")
                                                print("1. Add New Computer")
                                                print("2. Show Computer")
                                                print("3. Update Record")
                                                print("4. Delete Record")
                                                print("5. Search Record")
                                                print("6. Return")
                                                computer_entry_input = (
                                                    VALIDATORS.get_numeric("\n> ", 1, 6)
                                                )
                                                if computer_entry_input == 1:
                                                    # 1. Add New Computer
                                                    while True:
                                                        cpu = input(
                                                            "Please enter the cpu model :"
                                                        )
                                                        if cpu != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        ram = input(
                                                            "Please enter the ram size :"
                                                        )
                                                        if ram != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        gpu = input(
                                                            "Please enter the gpu model :"
                                                        )
                                                        if gpu != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        storage = input(
                                                            "Please enter the storage size :"
                                                        )
                                                        if storage != "":
                                                            break
                                                        print("Error : Empty input")

                                                    comp.Add_New_Computer(
                                                        cpu, ram, gpu, storage
                                                    )
                                                    cpu = None
                                                    ram = None
                                                    gpu = None
                                                    storage = None

                                                elif computer_entry_input == 2:
                                                    print(comp.Show_All_Computers())

                                                elif computer_entry_input == 3:
                                                    # 3. Update Record
                                                    while True:
                                                        computer_id = input(
                                                            "Please enter the computer ID :"
                                                        )
                                                        if computer_id != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        cpu = input(
                                                            "Please enter the cpu model :"
                                                        )
                                                        if cpu != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        ram = input(
                                                            "Please enter the ram size :"
                                                        )
                                                        if ram != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        gpu = input(
                                                            "Please enter the gpu model :"
                                                        )
                                                        if gpu != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        storage = input(
                                                            "Please enter the storage size :"
                                                        )
                                                        if storage != "":
                                                            break
                                                        print("Error : Empty input")

                                                    comp.Update_Record(
                                                        computer_id,
                                                        cpu,
                                                        ram,
                                                        gpu,
                                                        storage,
                                                    )
                                                    computer_id = None
                                                    cpu = None
                                                    ram = None
                                                    gpu = None
                                                    storage = None

                                                elif computer_entry_input == 4:
                                                    # 4. Delete Record
                                                    while True:
                                                        computer_id = int(
                                                            input(
                                                                "Please enter the computer ID :"
                                                            )
                                                        )
                                                        if computer_id != "":
                                                            break
                                                        print("Error : Empty input")
                                                    comp.Delete_Computer_by_index(
                                                        computer_id
                                                    )
                                                    computer_id = None

                                                elif computer_entry_input == 5:
                                                    # 5. Search Record
                                                    while True:
                                                        Key_word = input(
                                                            "What do you want to search about? "
                                                        )
                                                        if Key_word != "":
                                                            break
                                                        print("Error : Empty input")
                                                    print(comp.Search_Record(Key_word))
                                                    Key_word = None

                                        elif master_entry_input == 3:
                                            session_entry_input = None
                                            while session_entry_input != 3:
                                                os.system("clear")
                                                print("1. Start New Session")
                                                print("2. End Existing Session")
                                                print("3. Return")
                                                session_entry_input = (
                                                    VALIDATORS.get_numeric("\n> ", 1, 3)
                                                )
                                                if session_entry_input == 1:
                                                    user_name = (
                                                        VALIDATORS.get_user_name(
                                                            "Enter user name"
                                                        )
                                                    )
                                                    res = QUERIES.lookup_item(
                                                        "databases/users.json",
                                                        user_name,
                                                    )
                                                    if res != None:
                                                        session_obj = session(user_name)
                                                        session_obj.start_session()
                                                    else:
                                                        print(
                                                            colored(
                                                                "\nUSER DOES NOT EXIST EXCEPTION: user '{}' does not exist in '{}' database".format(
                                                                    user_name,
                                                                    "databases/users.json",
                                                                ),
                                                                "red",
                                                            )
                                                        )
                                                elif session_entry_input == 2:

                                                    session.end_session()

                                                elif session_entry_input == 3:
                                                    # 3. return
                                                    break

                                        elif master_entry_input == 4:
                                            # return option
                                            break

                                elif admin_input == 2:
                                    cafe_management_entry_input = None
                                    # cafe management options start here
                                    while cafe_management_entry_input != 4:
                                        os.system("clear")
                                        print("1. Bookings")
                                        print("2. Charges")
                                        print("3. Drinks")
                                        print("4. Return")
                                        cafe_management_entry_input = (
                                            VALIDATORS.get_numeric("\n> ", 1, 4)
                                        )
                                        if cafe_management_entry_input == 1:
                                            # bookings
                                            pass
                                        elif cafe_management_entry_input == 2:
                                            # charges
                                            pass
                                        elif cafe_management_entry_input == 3:
                                            # drinks management options start here
                                            drinks_entry_input = None
                                            while drinks_entry_input != 6:
                                                os.system("clear")
                                                print("1. Add New Drink")
                                                print("2. Show Drinks")
                                                print("3. Update Record")
                                                print("4. Delete Record")
                                                print("5. Search Record")
                                                print("6. Return")
                                                drinks_entry_input = (
                                                    VALIDATORS.get_numeric("\n> ", 1, 6)
                                                )
                                                if drinks_entry_input == 1:
                                                    # 1. Add New Drink
                                                    while True:
                                                        drink_name = input(
                                                            "Please enter the drink name :"
                                                        )
                                                        if drink_name != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        drink_Price = input(
                                                            "Please enter the drink Price :"
                                                        )
                                                        if drink_Price != "":
                                                            break
                                                        print("Error : Empty input")

                                                    drink.add_drink(
                                                        drink_name, drink_Price
                                                    )
                                                    drink_name = None
                                                    drink_Price = None

                                                elif drinks_entry_input == 2:
                                                    # 2. Show Drinks
                                                    print(drink.Show_All_Drinks())

                                                elif drinks_entry_input == 3:
                                                    # 3. Update Record
                                                    while True:
                                                        Drink_id = int(
                                                            input(
                                                                "Please enter the drink ID :"
                                                            )
                                                        )
                                                        if Drink_id != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        drink_name = input(
                                                            "Please enter the drink name :"
                                                        )
                                                        if drink_name != "":
                                                            break
                                                        print("Error : Empty input")

                                                    while True:
                                                        drink_Price = input(
                                                            "Please enter the drink Price :"
                                                        )
                                                        if drink_Price != "":
                                                            break
                                                        print("Error : Empty input")

                                                    drink.Update_Record(
                                                        Drink_id,
                                                        drink_name,
                                                        drink_Price,
                                                    )
                                                    drink_name = None
                                                    Drink_id = None
                                                    drink_Price = None

                                                elif drinks_entry_input == 4:
                                                    # 4. Delete Record
                                                    while True:
                                                        Drink_id = int(
                                                            input(
                                                                "Please enter the drink ID :"
                                                            )
                                                        )
                                                        if Drink_id != "":
                                                            break
                                                        print("Error : Empty input")
                                                    drink.Delete_Drink_by_index(
                                                        Drink_id
                                                    )
                                                    Drink_id = None

                                                elif drinks_entry_input == 5:
                                                    # 5. Search Record
                                                    while True:
                                                        Key_word = input(
                                                            "What do you want to search about? "
                                                        )
                                                        if Key_word != "":
                                                            break
                                                        print("Error : Empty input")
                                                    print(comp.Search_Record(Key_word))
                                                    Key_word = None

                                elif admin_input == 3:
                                    # logout admin
                                    break

                                os.system("clear")
                                print("1. master entry")
                                print("2. cafe management")
                                print("3. logout admin")
                                admin_input = VALIDATORS.get_numeric("\n> ", 1, 3)

                            if admin_input == 3:
                                # go out of role == admin check
                                break

                        elif role == "member":
                            print(
                                colored(
                                    "\nINVALID LOGIN EXCEPTION: admin users are only allowed to login to the system",
                                    "red",
                                )
                            )
                            print("\nChoose an option to continue:")
                            print("1. try to login again")
                            print("2. return")
                            option = VALIDATORS.get_numeric("> ", 1, 2)
                            if option == 1:
                                continue
                            elif option == 2:
                                # Terminate Progrm option
                                break
                    else:
                        # either entered password is valid or invalid. No more options here
                        break

                else:
                    # either user exist or does not exist in the users.json database. No more options here
                    break
        os.system("clear")
        print("1. Admin login")
        print("2. Terminate Progrm")
        main_input = VALIDATORS.get_numeric("\n> ", 1, 2)

    os.system("clear")
    exit()


if __name__ == "__main__":
    main()
