import random


# ////////////-------- INIT -----------//////////////////
class GamePlay:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num



# ////////////-------- ADD -----------//////////////////

class Addition(GamePlay):
    def __init__(self, first_num, second_num):
        super().__init__(first_num, second_num)
        self.realAns = first_num + second_num

    def checker(self, userAns):
        return "correct" if userAns == self.realAns else "Wrong"
            
    def __str__(self):
        return f"{self.first_num} + {self.second_num} = ?"
    
    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 20)
            if num != self.realAns:
                randomNums.add(num)
        randomNums.add(self.realAns)
        return f"----> {' '.join(map(str, randomNums))}"
    


# ////////////-------- SUBTRACTION -----------//////////////////

class Subtraction(GamePlay):
    def __init__(self, first_num, second_num):
        if first_num < second_num:
            first_num, second_num = second_num, first_num
        super().__init__(first_num, second_num)
        self.realAns = first_num - second_num

    def checker(self, userAns):
        return "correct" if userAns == self.realAns else "Wrong"
            
    def __str__(self):
        return f"{self.first_num} - {self.second_num} = ?"

    
    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 20)
            if num != self.realAns:
                randomNums.add(num)
        randomNums.add(self.realAns)
        return f"----> {' '.join(map(str, randomNums))}"
    

# ////////////-------- MULTIPLICATION -----------//////////////////

class Multiplication(GamePlay):
    def __init__(self, first_num, second_num):
        super().__init__(first_num, second_num)
        self.realAns = first_num * second_num

    def checker(self, userAns):
        return "correct" if userAns == self.realAns else "Wrong"
            
    def __str__(self):
        return f"{self.first_num} x {self.second_num} = ?"

    
    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 400)
            if num != self.realAns:
                randomNums.add(num)
        randomNums.add(self.realAns)
        return f"----> {' '.join(map(str, randomNums))}"
    

# ////////////-------- DIVISION -----------//////////////////

class Division(GamePlay):
    def __init__(self, first_num, second_num):
        if first_num < second_num:
            first_num, second_num = second_num, first_num
        super().__init__(first_num, second_num)
        self.realAns = round(first_num/second_num, 2)

    def checker(self, userAns):
        return "correct" if userAns == self.realAns else "Wrong"
            
    def __str__(self):
        return f"{self.first_num} ÷ {self.second_num} = ?"
    
    def randomAns(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = round(random.uniform(0, 20), 2)
            if num != self.realAns:
                randomNums.add(num)
        randomNums.add(self.realAns)
        return f"----> {' '.join(map(str, randomNums))}"

    

def main():
    a = random.randint(1,20)
    b = random.randint(1,20)

    print("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Quit")
    try:
        userChoise = int(input("---> "))
        if userChoise == 1:
            c = Addition(a, b)
            print(c)
            print(c.randomAns())

            userAns = float(input("=> "))
            print(c.checker(userAns))

        if userChoise == 2:
            c = Subtraction(a, b)
            print(c)
            print(c.randomAns())

            userAns = float(input("=> "))
            print(c.checker(userAns))

        if userChoise == 3:
            c = Multiplication(a, b)
            print(c)
            print(c.randomAns())

            userAns = float(input("=> "))
            print(c.checker(userAns))

        if userChoise == 4:
            c = Division(a, b)
            print(c)
            print(c.randomAns())

            userAns = float(input("=> "))
            print(c.checker(userAns))
        
        if userChoise == 5:
            print("Goodbye!")
            exit()
    
    except ValueError:
        print("Something went wrong!")
    
    
        

if __name__ == "__main__":
    main()