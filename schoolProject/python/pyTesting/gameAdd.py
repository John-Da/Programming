import random
import countdown as countDown
import gameMenu as menu


def gameAddition():
    score = 0
    chances = 3
    wrong_ans = 0
    run = True

    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)
    answer = num_1 + num_2
    print(f"{num_1} + {num_2} = ")
    guess = int(input('Ans: '))

    while run:
        if guess == answer:
            score += 2
            print('correct!')
            break
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
                        countDown()
                        menu()
                    elif choice == 'p':
                        print(f'You now have {chances} chances...\nGood luck!')
                        wrong_ans = 0
                        countDown()
                        gameAddition()
                    else:
                        print("Invalid input. Please enter 'p' to play (or) 'q' to quit.")


