def get_numeric(
    placeholder, value_type=None, min_value=None, max_value=None, max_length=10
):
    """
    Validate the numerical inputs.

    Parameters:
        placeholder (str): message displayed for user to input a value
        min_value (int): the minimum value for input
        max_value (int): the maximum value for input

    Returns:
        valid user input in integer
    """
    if min_value is not None and max_value is not None and max_value < min_value:
        raise ValueError("min_value must be less than or equal to max_value.")
    while True:
        user_input = input(placeholder)
        if value_type is not None:
            try:
                user_input = value_type(user_input)
            except ValueError:
                print("Input type must be {0}.".format(value_type.__name__))
                continue
            if len(str(user_input)) != 10:
                print("Input must be equal to {0} numbers.".format(max_length))
                continue
        if max_value is not None and user_input > max_value:
            print("Input must be less than or equal to {0}.".format(max_value))
        elif min_value is not None and user_input < min_value:
            print("Input must be greater than or equal to {0}.".format(min_value))
        else:
            if len(str(user_input)) == 10:
                user_input = "0" + str(user_input)
            return user_input


def get_password(placeholder):
    numbers_count = 0
    capital_letters_count = 0
    while True:
        password = input(placeholder)
        for char in password:
            if char.isnumeric():
                numbers_count += 1
            elif char.isupper():
                capital_letters_count += 1
        if len(password) < 8:
            print("password must have at least 8 letters")
        if numbers_count == 0:
            print("password must have at least 1 number")
        if capital_letters_count == 0:
            print("password must have at least 1 capital letter")
        else:
            return password


def get_string(placeholder):
    keyword = ""
    for char in placeholder:
        if char.isspace():
            if keyword == "name" or keyword == "tomodifiy":
                break
            else:
                keyword = ""
        elif char.isalpha():
            keyword = keyword + char

    while True:
        invalid_string = False
        input_string = input(placeholder)
        for char in input_string:
            if char.isnumeric():
                print("{} must be in letters only".format(keyword))
                invalid_string = True
                break
            if char.isspace():
                print("{} characters must be continous".format(keyword))
                invalid_string = True
                break
        if invalid_string:
            continue

        return input_string


def get_user_name(placeholder):
    while True:
        invalid_user_name = False
        user_name = input(placeholder)
        for char in user_name:
            if char.isspace():
                print("user name must be wriiten without spaces")
                invalid_user_name = True
                break
            if char.isnumeric() or char.isalpha() or char == "_":
                continue
            else:
                print("user name supports only underscores '_' as a special character")
                invalid_user_name = True
                break
        if invalid_user_name:
            continue
        return user_name


def get_address(placeholder):
    while True:
        invalid_address = False
        address = input(placeholder)
        for char in address:
            if (
                char.isnumeric()
                or char.isalpha()
                or char.isspace()
                or char == "_"
                or char == "-"
                or char == "."
                or char == ","
            ):
                continue
            else:
                invalid_address = True
                print(
                    "address supports only alphabet characters and '-', '_', ',' or '.' as special characters "
                )
                break
        if invalid_address:
            continue
        return address


def get_role(placeholder):
    while True:
        role = input(placeholder)
        if (
            role != "member"
            and role != "Member"
            and role != "admin"
            and role != "Admin"
        ):
            print("Member and admin are only supported roles in the system")
            continue
        return role.lower()
