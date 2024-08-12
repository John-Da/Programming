import random


def addition(self):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2
    self.problem['num1'] = num1
    self.problem['num2'] = num2
    self.problem['result'] = result
    self.operation = 'addition'


def substration(self):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    if num1 > num2:
        result = num1 - num2
        self.problem['num1'] = num1
        self.problem['num2'] = num2
        self.problem['result'] = result
    else:
        result = num2 - num1
        self.problem['num1'] = num1
        self.problem['num2'] = num2
        self.problem['result'] = result
    self.operation = 'substraction'

def multiplication(self):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 * num2
    self.problem['num1'] = num1
    self.problem['num2'] = num2
    self.problem['result'] = result
    self.operation = 'multiplication'


def division(self):
    divisor = random.randint(1,12)
    dividend = divisor * random.randint(1,12)
    result = dividend / divisor
    self.problem["num1"] = dividend
    self.problem["num2"] = divisor
    self.problem["result"] = result
    self.operation = "division"
