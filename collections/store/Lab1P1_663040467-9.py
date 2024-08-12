
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)





# def cal_fact(n):

#     fact = 1

#     for i in range(1, n+1):
#         fact = fact * i

#     return fact


n = int(input("Enter n: "))
result = factorial(n)
print(f"{n}! = {result}")