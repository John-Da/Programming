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