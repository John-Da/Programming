from gameLogin import login, choice, register
import gameMenu as mn

gameLines = './pyTesting/gameDiscription.txt'

with open(gameLines, 'r') as script:
    lines = script.read()
    print(lines)

if __name__ == "__main__":
    choice_register = input(str("Already Register? (Y / N): "))
    choice_register = str.lower(choice_register)
    if choice_register == 'n':
        if register() == True:
            login_successful, my_username = login()
            if login_successful:
                mn.menu()
            else:
                choice()
        else:
            register()
    elif choice_register == 'y':
        login_successful, my_username = login()
        if login_successful:
            mn.menu()
        else:
            choice()
    else:
        print("\nError")
        exit()