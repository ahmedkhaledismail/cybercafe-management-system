import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
import user
from databases import queries as queries
from project import constants as CONSTANTS
from project import helpers as HELPERS


class admin(user):
    def __init__(self, role, user_name, full_name):
        self.__full_name = full_name
        self.__role = role
        self.__user_name = user_name

    def __Show_Member(self):
        print(
            """
            Member Name is: {full_name} 
            Member role is: {user_role}
            """.format(
                full_name=self.__full_name, user_role=self.__role
            )
        )

    def __Add_New_Member():
        _user_id = None
        _user_name = None

        user_fullname = input("Enter user name: ")
        user_address = input("Enter user address: ")
        user_phone_number = input("Enter user address: ")
        user_password = input("Enter user password: ")
        user_role = input("Enter user role: ")
        user_age = input("Enter user age: ")
        user_name = HELPERS.get_user_name(user_fullname)
        response = queries.search_database_by_key(
            CONSTANTS.DATABASES["USERS_DATABASE"], user_name
        )
        if response == CONSTANTS.DATABASE_DOES_NOT_EXIST:
            print("ERROR: DATABASE_DOES_NOT_EXIST")
        elif response == CONSTANTS.KEY_EXIST:
            user_name = HELPERS.create_user_name(user_name)

        # quries include search update delete and append

        # TODO: check if the user_name does exist the the database. If so, raise an already registered error

    def __Update_Record():
        pass

    def __Search_Record():
        pass

    def __Delete_Record():
        pass


ahmed = admin("manager", "ahmed_khalid", "Ahmed Khalid Ismail")
ahmed._admin__Show_Member()
