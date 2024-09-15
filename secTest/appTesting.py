import database as userInfo


create_dataBase = False


def _userChoice():
    try:
        manageInfo = input("Update or Delete Account or See Info? (U/D/S): ")
        if manageInfo.lower() == "d":
            email = input("Enter email: ")
            _deleteUser(email)
        elif manageInfo.lower() == "u":
            _updateUser()
        elif manageInfo.lower() == "s":
            _seeUserInfo()
    except TypeError:
        print("Invalid email.")
    except ValueError:
        print("Invalid email.")


def _deleteUser(email):
    userInfo.delete_info(email)


def _seeUserInfo():
    try:
        userpassword = input("Enter password: ")
        userInfo.show_userInfo(userpassword)
    except TypeError:
        print("Invalid input")
    except ValueError:
        print("Invalid input")


def _updateUser():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    userInfo.update_userInfo(username, email, password)


def _signUp():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    userInfo.user_signUp(username, email, password)
    _userChoice()


def _logIn():
    email = input("Enter email: ")
    password = input("Enter password: ")
    userInfo.user_login(email, password)
    _userChoice()


def haveAccount():
    asked = input("Already have an account? (y/n): ")
    try:
        if asked.lower() == "y":
            _logIn()
        elif asked.lower() == "n":
            _signUp()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            haveAccount()  # Ask again if the input is invalid
    except TypeError:
        print("Invalid information.")
    except ValueError:
        print("Invalid information.")


def run_app():
    global create_dataBase
    try:
        if not create_dataBase:
            userInfo.create_dataBase()
            create_dataBase = True  # Set flag after creating the database
            haveAccount()
        elif create_dataBase:
            haveAccount()  # Prompt user after creating the database

    except Exception as e:
        print(f"An error occurred: {e}")  # Print any unexpected errors


if __name__ == "__main__":
    run_app()
