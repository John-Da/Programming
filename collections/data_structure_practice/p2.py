
while True:
    try:
        first_number = input("Enter the first number: ")
        first_number = float(first_number)
        if type(first_number) is float:
            while True:
                try:
                    second_number = input("Enter the second number: ")
                    second_number = float(second_number)
                    if type(second_number) is float:
                        operation = input("Enter the operation (+, -, *, /): ")
                        if operation == "/" and second_number == 0:
                            print("Error: Division by Zero")
                            exit()

                        elif operation == "+":
                            answer =  first_number + second_number
                            print(f"{first_number} {operation} {second_number} = {answer}")
                            exit()

                        elif operation == "-":
                            answer =  first_number - second_number
                            print(f"{first_number} {operation} {second_number} = {answer}")
                            exit()
                        elif operation == "/":
                            answer =  first_number / second_number
                            print(f"{first_number} {operation} {second_number} = {answer}")
                            exit()
                        elif operation == "*":
                            answer =  first_number * second_number 
                            print(f"{first_number} {operation} {second_number} = {answer}")
                            exit()      
                        else:
                            print("Error: Invalid operation")
                            exit()
                except ValueError:
                    if type(second_number) is str:
                        pass
    except ValueError:
        if type(first_number) is str:
            pass
            

            



























while True:
    try:
        first_number = input("Enter the first number: ")
        first_number = float(first_number)
        break
    except ValueError:
        ValueError

while True:
    try:
        second_number = input("Enter the second number: ")
        second_number = float(second_number)
        break
    
    except ValueError:
        ValueError

operation = input("Enter the operation (+, -, *, /): ")

if operation == "/" and second_number == 0:
    print("Error: Division by Zero")
else:
    if operation == "+":
        answer =  first_number + second_number
    if operation == "-":
        answer =  first_number - second_number
    if operation == "/":
        answer =  first_number / second_number
    if operation == "*":
        answer =  first_number * second_number       
    else:
        print("Error: Invalid operation")

print(f"{first_number} {operation} {second_number} = {answer}")

