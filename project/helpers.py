import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)
from project import constants as CONSTANTS
from databases import queries as QUERIES


def suggest_user_name(user_name):
    counter = 1
    while True:
        response = QUERIES.lookup_item(CONSTANTS.USERS_DATABASE, user_name)[1]
        if response == CONSTANTS.ITEM_EXIST:
            user_name = user_name + str(counter)
            counter += 1
            continue
        elif response == CONSTANTS.ITEM_DOES_NOT_EXIST:
            break

    return user_name
