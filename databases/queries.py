import sys

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from project import constants as CONSTANTS


def search_database_by_key(database, search_key):
    response = None
    for db in CONSTANTS.DATABASES:
        if db == database:
            response = CONSTANTS.DATABASE_EXIST
            for key in db:
                if key == search_key:
                    response = CONSTANTS.KEY_EXIST
    if response != CONSTANTS.DATABASE_EXIST or response != CONSTANTS.KEY_EXIST:
        response = CONSTANTS.DATABASE_DOES_NOT_EXIST
    else:
        response = CONSTANTS.KEY_DOES_NOT_EXIST
    return response
