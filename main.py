import os
import time

from project import validators as VALIDATORS
from project import constants as CONSTANTS
from project import helpers as HELPERS
from databases import queries as QUERIES

from classes.admin import admin
from classes.member import member


def main():
    print("\n\nWelcome to cybercafe management system\n\n")
    print("1. login")
    print("2. Don't have an account? Create an account")
    print("3. Terminate Progrm")
    user_input = VALIDATORS.get_numeric("\n> ", 1, 3)

    while user_input != CONSTANTS.PROGRAM_EXIT:
        if user_input == 1:
            user_input2 = None
            while user_input2 != CONSTANTS.RETURN:
                os.system("clear")
                user_name = VALIDATORS.get_user_name("Enter your user name: ")
                password = VALIDATORS.get_password("Enter your password: ")
                item_attributes, response = QUERIES.lookup_item(
                    CONSTANTS.USERS_DATABASE, user_name
                )
                while response == CONSTANTS.ITEM_DOES_NOT_EXIST:
                    print(
                        "\nERROR: item '{}' does not exist in '{}' database".format(
                            user_name, CONSTANTS.USERS_DATABASE
                        )
                    )
                    print("\nChoose an option to continue:")
                    print("1. try to login again")
                    print("2. return")
                    option = VALIDATORS.get_numeric("> ", 1, 2)
                    if option == 1:
                        user_name = VALIDATORS.get_user_name("Enter your user name: ")
                        password = VALIDATORS.get_password("Enter your password: ")
                        item_attributes, response = QUERIES.lookup_item(
                            CONSTANTS.USERS_DATABASE, user_name
                        )
                        print(response)
                    elif option == 2:
                        user_input2 = "return"
                        break
                if response == CONSTANTS.ITEM_EXIST:
                    stored_password = QUERIES.get_attribute(
                        CONSTANTS.USERS_DATABASE, user_name, "password"
                    )
                    if stored_password != password:
                        print("ERROR: you have written a wrong password, try again!")
                        time.sleep(4)
                        continue
                    elif stored_password == password:
                        first_name = item_attributes.get("first_name")
                        last_name = item_attributes.get("last_name")
                        print(
                            "SUCCESS: you have logged in to the system as {} {}".format(
                                first_name, last_name
                            )
                        )
                        # TODO: start sesssion for a logged in user if he is a member

                        time.sleep(4)

        elif user_input == 2:
            os.system("clear")
            first_name = VALIDATORS.get_name("\nEnter user first name: ")
            last_name = VALIDATORS.get_name("Enter user last name: ")
            user_name = VALIDATORS.get_user_name("Enter user name: ")

            res = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]
            while res == CONSTANTS.ITEM_EXIST:
                suggested_user_name = HELPERS.suggest_user_name(user_name)
                res = QUERIES.lookup_item(
                    CONSTANTS.USERS_DATABASE, suggested_user_name
                )[1]
                if res == CONSTANTS.ITEM_EXIST:
                    continue
                print(
                    "ERROR: user name '{}' is already registered, you can use '{}' as a user name".format(
                        user_name, suggested_user_name
                    )
                )
                user_name = VALIDATORS.get_user_name("\nEnter user name: ")
                res = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]

            age = VALIDATORS.get_numeric("Enter user age: ", 10)
            phone_number = VALIDATORS.get_phone_number("Enter user phone number: ")
            address = VALIDATORS.get_address("Enter user address: ")
            role = VALIDATORS.get_role("Enter user role (member or admin): ")
            password = VALIDATORS.get_password("Enter user password: ")

            user_attributes = {
                "first_name": first_name,
                "last_name": last_name,
                "user_name": user_name,
                "address": address,
                "phone_number": phone_number,
                "password": password,
                "role": role,
                "age": age,
            }

            if role == "admin":
                user_attributes["role"] = "admin"
                user_object = admin(**user_attributes)
            elif role == "member":
                user_attributes["role"] = "member"
                user_object = member(**user_attributes)

            print(
                "you have successufly created {} {} {} user".format(
                    first_name, last_name, role
                )
            )
            # TODO: pass control to the created account and starts new session in case of member user
            time.sleep(5)

        os.system("clear")
        print("1. login")
        print("2. Don't have an account? Create an account")
        print("3. Terminate Progrm")
        user_input = VALIDATORS.get_numeric("\n> ", 1, 4)

    exit()


main()
