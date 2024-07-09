

import countdown as count
# import menu


def register():
    with open("database.txt", "a") as add:
        with open("database.txt", "r") as data:
            print("\n------------Register----------")
            w_username = input("\nCreate your username: ")
            w_password = input("Create your password: ")
            w_con_password = input("Confirm password: ")
            list_username = []
            for user in data:
                username,password = user.split(",")
                list_username.append(username)
            if w_password != w_con_password :
                print("\nPassword don't match!!")
                register()
            else :
                if len(w_password) < 6 :
                    print("\nPassword too short!!")
                    register()
                elif w_username in list_username:
                    print("\nUsername exists!!")
                    register()
                else :
                    print("\nregister succsess!!")
                    add.write(w_username+", "+(w_password)+"\n")
    return True

def login():
    with open("database.txt", "r") as read:
        print("\n-----------Login-----------")
        w_username = input("\nEnter your username: ")
        w_password = input("Enter your password: ")
        dict_username = []
        dict_password = []
        try:
            for user in read:
                username,password = user.split(",")
                password = password.strip()
                dict_username.append(username)
                dict_password.append(password)
                data = dict(zip(dict_username, dict_password))

            if w_username in data:
                username_corect = True
                if w_password == data[w_username]:
                    password_corect = True
                else:
                    password_corect = False
            else:
                username_corect = False

            if username_corect == True and password_corect == True :
                print("\nLogin success!")
                print(f"Welcome {w_username}")
                count.countdown()
                return True , w_username
            else :
                print("\nLogin failed")
                return False , None
        except:
            print("\nLogin failed")
            count.countdown()
            
            
def choice():
    while True :
        choice_try = input(str("\nYour want to try again or exit? (T or E): "))
        choice_try = str.lower(choice_try)
        if choice_try == "t":
            choice_try2 = input(str("\nyou want to register or login? (R or L): "))
            choice_try2 = str.lower(choice_try2)
            if choice_try2 == "r":
                if register() == True:
                    login_successful, my_username = login()
                    if login_successful:
                        menu()
                        break
                    else :
                        choice()
                else :
                    register()
            elif choice_try2 == "l":
                login_successful, my_username = login()
                if login_successful:
                    menu()
                    break
                else :
                    choice()
            else :
                print("\nError")
                break
        elif choice_try == "e" :
            print("\nSee you")
            break
        else :
            print("\nError")
            break
            
register()
login()      