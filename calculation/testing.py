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
        self.realanswer = first_num + second_num
    
    def checker(self, user_answer):
        if user_answer == self.realanswer:
            return True
        else:
            return False
        
    def __str__(self):
        
        return f"{self.first_num} + {self.second_num} = ?"
    
    def randomanswer(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 20)
            if num != self.realanswer:
                randomNums.add(num)
        randomNums.add(self.realanswer)
        return f"{' '.join(map(str, randomNums))}"

# ////////////-------- SUBTRACTION -----------//////////////////

class Subtraction(GamePlay):
    def __init__(self, first_num, second_num):
        if first_num < second_num:
            first_num, second_num = second_num, first_num
        super().__init__(first_num, second_num)
        self.realanswer = first_num - second_num

    def checker(self, user_answer):
        if user_answer == self.realanswer:
            return True
        else:
            return False
            
    def __str__(self):
        return f"{self.first_num} - {self.second_num} = ?"

    
    def randomanswer(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 20)
            if num != self.realanswer:
                randomNums.add(num)
        randomNums.add(self.realanswer)
        return f"{' '.join(map(str, randomNums))}"
    
# ////////////-------- MULTIPLICATION -----------//////////////////

class Multiplication(GamePlay):
    def __init__(self, first_num, second_num):
        super().__init__(first_num, second_num)
        self.realanswer = first_num * second_num

    def checker(self, user_answer):
        if user_answer == self.realanswer:
            return True
        else:
            return False
            
    def __str__(self):
        return f"{self.first_num} x {self.second_num} = ?"

    
    def randomanswer(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = random.randint(0, 400)
            if num != self.realanswer:
                randomNums.add(num)
        randomNums.add(self.realanswer)
        return f"{' '.join(map(str, randomNums))}"
    
# ////////////-------- DIVISION -----------//////////////////

class Division(GamePlay):
    def __init__(self, first_num, second_num):
        if first_num < second_num:
            first_num, second_num = second_num, first_num
        super().__init__(first_num, second_num)
        self.realanswer = round(first_num/second_num, 2)

    def checker(self, user_answer):
        if user_answer == self.realanswer:
            return True
        else:
            return False
            
    def __str__(self):
        return f"{self.first_num} ÷ {self.second_num} = ?"
    
    def randomanswer(self):
        randomNums = set()
        while len(randomNums) < 3:
            num = round(random.uniform(0, 20), 2)
            if num != self.realanswer:
                randomNums.add(num)
        randomNums.add(self.realanswer)
        return f"{' '.join(map(str, randomNums))}"


def main():
    point = 0
    chance = 3
    while True:
        a = random.randint(1,20)
        b = random.randint(1,20)
        c = Subtraction(a, b)
        print(c)
        print(c.randomanswer())
        userAns = float(input("Enter your answer: "))
        if c.checker(userAns) == True:
            point += 1
            print("---------------------------------------------------------------------------------")
            print("\ncorrcet")
            print(f"Your corrent point = {point}")
            print("\n---------------------------------------------------------------------------------\n")
        else:
            chance -= 1
            if chance == 0:
                print("\n---------------------------------------------------------------------------------")
                print("\nIncorrect")
                print(f"Your total point = {point}")
                print("Game over!!")
                print("\n---------------------------------------------------------------------------------")
                break
            print("\n---------------------------------------------------------------------------------")
            print("\nIncorrect")
            print(f"Your corrent point = {point}")
            print(f"Your chance = {chance}")
            print("\n---------------------------------------------------------------------------------")           

if __name__ == "__main__":
    main()