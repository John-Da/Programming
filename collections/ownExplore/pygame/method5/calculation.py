#for addition
import random
number = [1,2,3,4,5,6,7,8,9,10]

chance = 3
point = 0

while True:
    number1 = random.choice(number)
    number2 = random.choice(number)
    answer = number1 + number2
    print(f"num1 = {number1} and num2 = {number2}, Answer is {answer}")

    get_input = input("Please enter your stupid answer: ")
    # get_input = int(get_input)
    
    try:
        if type(get_input) is int:
            if get_input == answer:
                point += 1
                print(point)
                print(f"your point is {point} ")

        else:
            chance -= 1 
            print(f"your chance is {chance})")
            if chance == 0 :
                break
    except ValueError:
        print("Please enter integer number\nTry It Agian!!")
        chance -= 1
        if chance == 0 :
            break
