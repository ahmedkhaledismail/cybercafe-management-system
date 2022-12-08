import os
import time
from termcolor import colored

from project import validators as VALIDATORS
from project import constants as CONSTANTS
from databases import queries as QUERIES

import classes.admin as ADMIN

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
#         Renewal
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
                user_attributes, response = QUERIES.lookup_item(
                    CONSTANTS.USERS_DATABASE, user_name
                )
                while response == CONSTANTS.ITEM_DOES_NOT_EXIST:
                    print(
                        colored(
                            "\nUSER DOES NOT EXIST EXCEPTION: user '{}' does not exist in '{}' database".format(
                                user_name, CONSTANTS.USERS_DATABASE
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
                        user_attributes, response = QUERIES.lookup_item(
                            CONSTANTS.USERS_DATABASE, user_name
                        )
                    elif option == 2:
                        # Terminate Progrm option
                        break
                if response == CONSTANTS.ITEM_EXIST:
                    stored_password = QUERIES.get_attribute(
                        CONSTANTS.USERS_DATABASE, user_name, "password"
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
                                CONSTANTS.USERS_DATABASE, user_name
                            )[0]
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
                                    while master_entry_input != 3:
                                        os.system("clear")
                                        print("1. member entry")
                                        print("2. computer entry")
                                        print("3. return")
                                        master_entry_input = VALIDATORS.get_numeric(
                                            "\n> ", 1, 3
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
                                                    pass
                                                elif member_entry_input == 2:
                                                    # 2. Show Member
                                                    pass
                                                elif member_entry_input == 3:
                                                    # 3. Update Record
                                                    pass
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
                                                    pass
                                                elif computer_entry_input == 2:
                                                    # 2. Show Computer
                                                    pass
                                                elif computer_entry_input == 3:
                                                    # 3. Update Record
                                                    pass
                                                elif computer_entry_input == 4:
                                                    # 4. Delete Record
                                                    pass
                                                elif computer_entry_input == 5:
                                                    # 5. Search Record
                                                    pass

                                        elif master_entry_input == 3:
                                            # return option
                                            break

                                elif admin_input == 2:
                                    cafe_management_entry_input = None
                                    # cafe management options starts here
                                    while cafe_management_entry_input != 4:
                                        os.system("clear")
                                        print("1. Bookings")
                                        print("2. Charges")
                                        print("3. Renewal")
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
                                            # renewal
                                            pass

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


main()
