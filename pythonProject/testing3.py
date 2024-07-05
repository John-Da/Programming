import random
import operator


def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)

    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'{num_1} {operation} {num_2} = ')
    return answer


def ask_question():
    answer = int(random_problem())
    guess = float(input('Ans: '))
    return guess == answer


def game():
    score = 0
    correct_ans = 0
    wrong_ans = 0
    while True:
        if ask_question() == True:
            score += 1
            correct_ans += 1
            print('correct!')
        else:
            print('Incorrect')
            wrong_ans += 1
            break
    
    print(f'======= Game Over =========\nYour score is {score}\nCorrect: {correct_ans}\nWrong: {wrong_ans}')

game()