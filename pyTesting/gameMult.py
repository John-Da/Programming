import randomNum as random_num
import countdown as countDown
import gameMenu as menu

score = 0


def addition():
    num_1, num_2 = random_num()
    answer = num_1 + num_2
    print(f"{num_1} + {num_2} = ")
    guess = int(input('Ans: '))
    return guess == answer

def game():
    score = 0
    chances = 3
    # correct_ans = 0
    wrong_ans = 0
    run = True
    while run:
        if addition() == True:
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
                        countDown()
                        menu()
                    elif choice == 'p':
                        print(f'You now have {chances} chances...\nGood luck!')
                        wrong_ans = 0
                        countDown()
                        game()
                    else:
                        print("Invalid input. Please enter 'p' to play (or) 'q' to quit.")


