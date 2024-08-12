# print('\n'.join([f'{i}! = {1 if i == 0 else i * (lambda fact, x: fact(fact, x))(lambda fact, x: 1 if x <= 1 else x * fact(fact, x-1), i)}' for i in range(1, 11)]))


factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
counter = lambda count: print(
    "\n".join(f"{i}! = {factorial(i)}" for i in range(1, count + 1))
)
counter(int(input("Enter n: ")))
