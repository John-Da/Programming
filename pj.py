# main loop

if __name__ == "__main__":
  while True:
      try:
          userChoice = input("Choose (+, -, *, /): ")
          if (
              userChoice == "+"
              or userChoice == "-"
              or userChoice == "*"
              or userChoice == "/"
          ):
              pass
          else:
              raise ValueError
          break
      except ValueError:
          print("Valid Choice...")

  if userChoice == "+":
      # addtion()
      print("This is Addition")
  if userChoice == "-":
      # subtraction()
      print("This is Substraction")
  if userChoice == "*":
      # multiplication()
      print("This is Multiplication")
  if userChoice == "/":
      # division()
      print("This is Division")


# if __name__ == "__main__":
#     while True:
#         if userChoice == '+':
#             addtion()
#         if userChoice == '-':
#             subtraction()
#         if userChoice == '*':
#             multiplication()
#         if userChoice == '/':
#             division()


# if userChoice == '+':
#     ran1 = random.randint(0,30)
#     ran2 = random.randint(0,30)
#     addtionAns = add(ran1, ran2)
#     if user_answer == addtionAns:
#         totalScore += scoreAdd
#     else:
#         totalScore = totalScore

# if userChoice == '-':
#     ran1 = random.randint(0,30)
#     ran2 = random.randint(0,30)
#     subtractionAns = subtract(ran1, ran2)
#     if user_answer == subtractionAns:
#         totalScore += scoreAdd
#     else:
#         totalScore = totalScore

# if userChoice == '*':
#     ran1 = random.randint(0,30)
#     ran2 = random.randint(0,30)
#     multiplicationAns = multiply(ran1, ran2)
#     if user_answer == multiplicationAns:
#         totalScore += scoreAdd
#     else:
#         totalScore = totalScore

# if userChoice == '/':
#     ran1 = random.randint(0,30)
#     ran2 = random.randint(0,30)
#     divisionAns = divide(ran1, ran2)
#     if user_answer == divisionAns:
#         totalScore += scoreAdd
#     else:
#         totalScore = totalScore


# test
import time


loopTime = True


def countDown(t):
  while t:
      mins, secs = divmod(t, 60)
      timer = "{:02d}:{:02d}".format(mins, secs)
      time.sleep(1)
      print(timer, end="\r")
      t -= 1
  print("Time Up")
  loopTime = False
  return loopTime


timeUp = 5
if countDown(timeUp) is False:
  print("stopped")

else:
  print("going")


# countdown
import time


def countDown(t):
  while t:
      mins, secs = divmod(t, 60)
      timer = "{:02d}:{:02d}".format(mins, secs)
      time.sleep(1)
      print(timer, end="\r")
      t -= 1
  return False


# Loop
# files import
# from operation import add
# from countDown import countDown


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


# totalScore = 0
# scoreAdd = 2

# # Addtion
# def addtion():
#     while ran:
# print("You will now have 1 mins to collect your scores.\nTo Quite, press 'Q'\nGood Luck...")
# countDown(startCountDown)
#         try:
#             addtionAns = add()
#             user_answer = input("Your Answer: ")
#             if user_answer == addtionAns:
#                 totalScore += scoreAdd
#             else:
#                 totalScore = totalScore
#         except ValueError:
#             print("Please Enter Positiive Number!")

# Operation


def add(num1, num2):
  return num1 + num2


def subtract(num1, num2):
  return num1 - num2


def multiply(num1, num2):
  return num1 * num2


def divide(num1, num2):
  return num1 / num2


# print(add(num1, num2))
# print(subtract(num1, num2))
# print(multiply(num1, num2))
# print(divide(num1, num2))
