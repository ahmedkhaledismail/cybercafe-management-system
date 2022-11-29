import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
from user import user
from member import member

from databases import queries as queries
from project import constants as CONSTANTS
from project import helpers as HELPERS
from project import validators as validators
from databases import queries as queries


class admin(user):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_member(self, member_user_name):
        member_attributes, response = queries.lookup_item(
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

    def add_new_member(self, member_attributes):
        role = member_attributes.get("role")
        user_name = member_attributes.get("user_name")
        response = queries.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]
        while response == CONSTANTS.KEY_EXIST:
            suggested_user_name = HELPERS.suggest_user_name(user_name)
            print(
                "ERROR admin.add_new_member(): user name '{}' is already registered, you can use '{}' as a user name".format(
                    user_name, suggested_user_name
                )
            )
            user_name = validators.get_user_name("Enter user name: ")

        if role == "admin":
            member_object = admin(**member_attributes)
        elif role == "member":
            member_object = member(**member_attributes)

        return member_object

    def update_record(self, user_name, key, value):
        queries.update_attribute(CONSTANTS.USERS_DATABASE, user_name, key, value)

    def search_record(self):
        pass

    def delete_record(self, user_name):
        queries.delete_item(CONSTANTS.USERS_DATABASE, user_name)
