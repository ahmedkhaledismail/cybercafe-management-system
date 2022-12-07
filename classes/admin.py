import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from classes.member import member
from classes.user import user
from project import constants as CONSTANTS
from project import validators as VALIDATORS
from project import helpers as HELPERS
from databases import queries as QUERIES


class admin(user):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_member(self, member_user_name):
        member_attributes, response = QUERIES.lookup_item(
            CONSTANTS.USERS_DATABASE, member_user_name
        )
        if response == CONSTANTS.ITEM_EXIST:
            for key, value in member_attributes.items():
                print("member {} is {}".format(key, value))
        elif response == CONSTANTS.ITEM_DOES_NOT_EXIST:
            print(
                "ERROR admin.show_member(): the item '{}' does not exist in the '{}' database".format(
                    member_user_name, CONSTANTS.USERS_DATABASE
                )
            )

    def add_new_member(self):
        first_name = VALIDATORS.get_name("\nEnter user first name: ")
        last_name = VALIDATORS.get_name("Enter user last name: ")
        user_name = VALIDATORS.get_user_name("Enter user name: ")

        res = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]
        while res == CONSTANTS.ITEM_EXIST:
            suggested_user_name = HELPERS.suggest_user_name(user_name)
            res = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, suggested_user_name)[1]
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
            member_object = admin(**user_attributes)
        elif role == "member":
            # member_object = member(**user_attributes)
            pass
        print(
            "you have successufly created {} {} {} user".format(
                first_name, last_name, role
            )
        )
        return member_object

    def update_record(self, user_name, key, value):
        QUERIES.update_attribute(CONSTANTS.USERS_DATABASE, user_name, key, value)

    def search_record(self):
        pass

    def delete_record(self, user_name):
        QUERIES.delete_item(CONSTANTS.USERS_DATABASE, user_name)


def construct_object(user_attributes):
    if user_attributes["role"] == "admin":
        constructed_object = admin(**user_attributes)
    elif user_attributes["role"] == "member":
        constructed_object = member(**user_attributes)
        pass
    return constructed_object
