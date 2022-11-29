import os
import time

from project import validators as VALIDATORS
from project import constants as CONSTANTS
from databases import queries as QUERIES


def main():
    print("\n\nWelcome to cybercafe management system\n\n")
    print("1. login as a member")
    print("2. login as an admin")
    print("3. Don't have an account? Create your account")
    print("4. Terminate Progrm")
    user_input = VALIDATORS.get_numeric("> ", int, 1, 4)

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
                    option = VALIDATORS.get_numeric("> ", int, 1, 2)
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

        os.system("clear")
        print("1. login as a member")
        print("2. login as an admin")
        print("3. Don't have an account? Create your account")
        print("4. Terminate Progrm")
        user_input = VALIDATORS.get_numeric("> ", int, 1, 4)

    exit()


main()
