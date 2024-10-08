import random
import operator
from termcolor import colored


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
    if operation == '/':
        answer = round(answer, 2)
    print(f'{num_1} {operation} {num_2} = ')
    print(answer)
    return answer


def ask_question():
    answer = float(random_problem())
    guess = float(input('Ans: '))
    return guess == round(answer, 2)


def countDown():
    pass


def game():
    score = 0
    chances = 3
    # correct_ans = 0
    wrong_ans = 0
    run = True
    while run:
        if ask_question() == True:
            score += 2
            # correct_ans += 1
            print('correct!')
        else:
            wrong_ans += 1
            print('Incorrect')
            print(f'You only have {chances - wrong_ans} chances now!')
            if wrong_ans == chances:
                print(f'======= Game Over =========\nYour score is {score}')
                while True:
                    choice = input("Play Again or Quit (P / Q): ").strip().lower()
                    if choice == 'q':
                        run = False
                        print('See you again!')
                        exit()
                    elif choice == 'p':
                        print(f'You now have {chances} chances...\nGood luck!')
                        wrong_ans = 0
                        game()
                    else:
                        print("Invalid input. Please enter 'p' to play (or) 'q' to quit.")
   
    # print('See you again!')
    # print(f'======= Game Over =========\nYour score is {score}')
    # print(f'======= Game Over =========\nYour score is {score}\nCorrect: {correct_ans}\nWrong: {wrong_ans}')


if __name__ == "__main__":
    text = colored('\n***=========================\n\nNote:  If your answer is (16/16 = 1), enter 1.0 and\n if ( 2/17 = 0.2323445 ), round the answer into 2 decimal, like (0.23)\n\n===================***\n', 'black', 'on_white')
    print(text)
    game()