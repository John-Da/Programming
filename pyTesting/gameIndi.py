import randomNum as random_num


score = 0


def addition():
    num_1, num_2 = random_num()
    answer = num_1 + num_2
    print(f"{num_1} + {num_2} = ")
    guess = int(input('Ans: '))
    return guess == answer

while True:
    if addition() == True:
        score += 1
        print(f"your score: {score}")
    else:
        score = score
        print(f"your score: {score}")


# def substraction():
#     pass

# def multiplication():
#     pass

# def division():
#     pass


addition()