from operator import add
from countDown import countDown

import random


# random number
num1 = random.randint(0, 30)
num2 = random.randint(0, 30)


# score data
totalScore = 0
scoreAdd = 2

# loop Function
loopCountDown = 60
loopTime = True


# addition loop
while loopTime:
  try:
      startCountDown = 5
      print(
          "You will now have 1 mins to collect your scores.\nTo Quit, press 'Q'\nGood Luck..."
      )
      if countDown(startCountDown) is False:
          print("Start...")

          numadd = f"{num1} + {num2} = "
          print(numadd)

          user_answer = input("Your Answer: ")
          if user_answer.lower() == "q":
              print("Stopped to Quit")
              break
          else:
              addtionAns = add(num1, num2)
              if user_answer == addtionAns:
                  totalScore += scoreAdd
                  print("Correct")
              else:
                  totalScore = totalScore
                  print("Try Better")

      if countDown(loopCountDown) is False:
          loopTime = False
          print("Time Up")
          break

  except ValueError:
      print("Please Enter Positiive Number!")