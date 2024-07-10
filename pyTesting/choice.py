# import 


# def choice():
#     while True :
#         choice_try = input(str("\nYour want to try again or exit? (T or E): "))
#         choice_try = str.lower(choice_try)
#         if choice_try == "t":
#             choice_try2 = input(str("\nyou want to register or login? (R or L): "))
#             choice_try2 = str.lower(choice_try2)
#             if choice_try2 == "r":
#                 if register() == True:
#                     login_successful, my_username = login()
#                     if login_successful:
#                         menu()
#                         break
#                     else :
#                         choice()
#                 else :
#                     register()
#             elif choice_try2 == "l":
#                 login_successful, my_username = login()
#                 if login_successful:
#                     menu()
#                     break
#                 else :
#                     choice()
#             else :
#                 print("\nError")
#                 break
#         elif choice_try == "e" :
#             print("\nSee you")
#             break
#         else :
#             print("\nError")
#             break