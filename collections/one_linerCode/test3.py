print("\n".join([f"{i:10}! = {1 if i == 0 else i * (lambda f, x: f(f, x))(lambda f, x: 1 if x <= 1 else x * f(f, x-1), i):10}" for i in range(1, 11)]))
