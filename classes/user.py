import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
from project import constants as CONSTANTS


class user:
    def __init__(self, **kwargs):
        self.__first = kwargs.get("first")
        self.__last = kwargs.get("last")
        self.__phone_number = kwargs.get("phone_number")
        self.__address = kwargs.get("address")
        self.__age = kwargs.get("age")
        self.__role = kwargs.get("role")
        self.__password = kwargs.get("password")
        self.__user_id = self.__create_user_id()

    @property
    def fullname(self):
        return "{} {}".format(self.__first, self.__last)

    @fullname.setter
    def fullname(self, fullname):
        first, last = fullname.split(" ")
        self.__first = first
        self.__last = last

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    def __create_user_id(self):
        CONSTANTS.USER_ID += 1
        return CONSTANTS.USER_ID
