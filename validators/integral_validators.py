def validate_integer(
    placeholder, value_type=None, min_value=None, max_value=None, value_range=None
):
    """
    Validate the integeral inputs.

    Parameters:
        placeholder (str): message displayed for user to input a value
        min_value (int): the minimum value for input
        max_value (int): the maximum value for input
        value_range (int): the maximum value for input

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
        if max_value is not None and user_input > max_value:
            print("Input must be less than or equal to {0}.".format(max_value))
        elif min_value is not None and user_input < min_value:
            print("Input must be greater than or equal to {0}.".format(min_value))
        elif value_range is not None and user_input not in value_range:
            if isinstance(value_range, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(value_range))
            else:
                template = "Input must be {0}."
                if len(value_range) == 1:
                    print(template.format(*value_range))
                else:
                    expected = " or ".join(
                        (
                            ", ".join(str(x) for x in value_range[:-1]),
                            str(value_range[-1]),
                        )
                    )
                    print(template.format(expected))
        else:
            return user_input
