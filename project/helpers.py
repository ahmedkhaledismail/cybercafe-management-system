import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
from project import constants as CONSTANTS
import databases.queries as queries


def get_user_name(fullname):
    """
    converts the full name into a user name

    Parameters:
        fullname (str): user full name seprated by white spaces

    Returns:
        full name after converting whitespaces to underscores and capital letters to lowercase letters
    """
    user_name = ""
    for char in fullname:
        if char.isspace():
            user_name = user_name + "_"
        elif char.isalpha():
            user_name = user_name + char.lower()

    return user_name


def create_user_name(user_name):
    """
    create a unique name from given user name such that new user name does not exist in the database

    Parameters:
        user_name (str): user name after applying user name standards

    Returns:
        unique user name that does not exist as a key in the database
    """
    counter = 0
    while True:
        user_name = user_name + str(counter)
        response = queries.search_database_by_key(
            CONSTANTS.DATABASES["USERS_DATABASE"], user_name
        )
        if response == CONSTANTS.KEY_DOES_NOT_EXIST:
            break
        if response == CONSTANTS.KEY_EXIST:
            counter += 1
            continue

    return user_name
