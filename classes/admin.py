import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from classes.user import user
from classes.member import member

from project import constants as CONSTANTS
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

    def add_new_member(self, **member_attributes):
        role = member_attributes.get("role")
        user_name = member_attributes.get("user_name")
        response = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]
        if response == CONSTANTS.ITEM_DOES_NOT_EXIST:
            if role == "admin":
                member_object = admin(**member_attributes)
            elif role == "member":
                member_object = member(**member_attributes)
            return member_object
        elif response == CONSTANTS.ITEM_EXIST:
            print("ERROR: user name '{}' is already registered".format(user_name))

    def update_record(self, user_name, key, value):
        QUERIES.update_attribute(CONSTANTS.USERS_DATABASE, user_name, key, value)

    def search_record(self):
        pass

    def delete_record(self, user_name):
        QUERIES.delete_item(CONSTANTS.USERS_DATABASE, user_name)
