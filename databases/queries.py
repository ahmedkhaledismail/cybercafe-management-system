import sys
import json

sys.path.insert(
    1,
    "/Users/ahmedkhaled/Desktop/Ahmed Khalid/MSA University/Computer Engineering/Third Year/First Semester/Concepts of Programming Languages/project/CybercafeManagementSystem",
)

from project import constants as CONSTANTS


def lookup_item(database, item):
    with open(database, "r") as json_database:
        dict_database = json.load(json_database)
        for entry in dict_database:
            for item_name in entry:
                if item_name == item:
                    return entry[item_name], CONSTANTS.ITEM_EXIST
    return None, CONSTANTS.ITEM_DOES_NOT_EXIST


def get_attribute(database, item, key):
    item_attributes, response = lookup_item(database, item)
    if response == CONSTANTS.ITEM_EXIST:
        return item_attributes[key]


def get_item_index(database, item):
    count = 0
    item_found = False
    with open(database, "r") as json_database:
        dict_database = json.load(json_database)
        for entry in dict_database:
            for item_name in entry:
                if item_name == item:
                    item_found = True
                    index = count
                    break
                elif item_name != item:
                    count += 1
            if item_found:
                break
    if item_found:
        return index
    return None


def update_attribute(database, item, key, value):
    json_database = open(database, "r")
    updated_dict_database = json.load(json_database)
    json_database.close()
    item_index = get_item_index(database, item)
    if item_index != None:
        updated_dict_database[item_index][item][key] = value
        jsonFile = open(database, "w+")
        jsonFile.write(json.dumps(updated_dict_database, indent=4))
        jsonFile.close()
    elif item_index == None:
        print(
            "ERROR update_attribute(): the item '{}' does not exist in the '{}' database".format(
                item, database
            )
        )


def get_item_name(kwargs):
    for key, value in kwargs.items():
        if key == "user_name":
            return value


def save_item(database, item_attributes):
    with open(database, "r") as f:
        json_database = json.load(f)
    item_name = get_item_name(item_attributes)
    response = lookup_item(database, item_name)[1]
    if response == CONSTANTS.ITEM_EXIST:
        print(
            "ERROR save_item(): the item {} already exists in the {} database".format(
                item_name, database
            )
        )
        return
    if item_name != None:
        item_entry = {item_name: item_attributes}
        json_database.append(item_entry)
        with open(database, "w") as f:
            json.dump(json_database, f, indent=4)

        print(
            "item '{}' has been successful saved into the '{}' database".format(
                item_name, database
            )
        )
    elif item_name == None:
        print(
            "ERROR save_item(): the item name does not exist in the given dictionary attributes"
        )


def delete_item(database, item):
    index = get_item_index(database, item)
    if index == None:
        print(
            "ERROR delete_item(): item '{}' does not exist in the '{}' database".format(
                item, database
            )
        )
    elif index != None:
        with open(database, "r") as f:
            json_database = json.load(f)
        del json_database[index]
        with open(database, "w") as f:
            json.dump(json_database, f, indent=4)
