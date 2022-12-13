import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
from project import constants as CONSTANTS
from project import queries as QUERIES


class user:
    def __init__(self, **kwargs):
        self.__first_name = kwargs.get("first_name")
        self.__last_name = kwargs.get("last_name")
        self.__phone_number = kwargs.get("phone_number")
        self.__address = kwargs.get("address")
        self.__age = kwargs.get("age")
        self.__role = kwargs.get("role")
        self.__password = kwargs.get("password")
        self.__user_name = kwargs.get("user_name")
        self.__user_id = self.__create_user_id()
        res = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, self.__user_name)[1]
        if res == CONSTANTS.ITEM_DOES_NOT_EXIST:
            QUERIES.save_item(CONSTANTS.USERS_DATABASE, kwargs)

    @property
    def fullname(self):
        return "{} {}".format(self.__first_name, self.__last_name)

    @fullname.setter
    def fullname(self, fullname):
        first_name, last_name = fullname.split(" ")
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "phone_number",
            phone_number,
        )

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "address",
            address,
        )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "age",
            age,
        )

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "role",
            role,
        )

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "password",
            password,
        )

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id
        QUERIES.update_attribute(
            CONSTANTS.USERS_DATABASE,
            self.__user_name,
            "user_id",
            user_id,
        )

    def __create_user_id(self):
        CONSTANTS.USER_ID += 1
        return CONSTANTS.USER_ID
