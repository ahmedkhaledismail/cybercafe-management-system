from validators.integral_validators import validate_integer
import project.constants as constants


def main():
    print(
        """
        Welcome to cybercafe management system

        1. login as a user 
        2. login as an admin
        3. Don't have an account? Create your account
        4. Terminate Progrm
        """
    )
    user_input = validate_integer("> ", int, 1, 4)
    if user_input == constants.PROGRAM_EXIT:
        exit()

    while user_input != constants.PROGRAM_EXIT:
        """if user_input == 1:
            user_login.user_login()
        elif user_input == 2:
            admin_login.admin_login()
        elif user_input == 3:
            create_account()"""


main()
