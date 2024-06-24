

def fun1(n):
    z = 0
    if (n > 1):
        fun1(n - 1)
    for z in range(n):
        print('*', end=' ')


fun1(5)


# def fun2(n):
#     if n == 0:
#         return 
    
#     fun2(n//2)
#     print(n % 2, end="")


# fun2(100)


# def f(x):
#     if x == 0:
#         return 0
#     else:
#         return 2 * f(x-1) + x * x
    


# fn = float(input("Enter a number: "))
# print("f(5) = ", f(fn))