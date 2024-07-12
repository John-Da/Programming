#game Choices
import gameScore
import allOfThem
import gameAdd as addition
import gameSubt as subtraction
import gameMult as multiplication
import gameDivi as division


def menu(): 
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) All of Them")
    print("6) Score Board")
    choice_games = input("What would you want to play? (1,2,3,4,5,6): ")
    if choice_games == "1" :
        addition.gameAddition()
    elif choice_games == "2":
        subtraction()
    elif choice_games == "3":
        multiplication()
    elif choice_games == "4":
        division()
    elif choice_games == "5":
        allOfThem()
    elif choice_games == "6":
        # gameScore(point,my_username)
        gameScore()
    elif choice_games == "6" :
        print("\nSee you")
        exit()
    else :
        print("\nError")
        exit()