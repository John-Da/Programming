


# print(123456//10)


# def digit(n):
#     print(n, end="")


# def printOut(n):
#     if n >= 10:
#         printOut(n//10)
#     digit(n % 10)


# n = int(input("n: "))
# printOut(n)



# def fun1(n):
#     z = 0
#     if (n > 1):
#         fun1(n - 1)
#     for z in range(n):
#         print('*', end=' ')


# fun1(5)


# def fun2(n):
#     if n == 0:
#         return 
    
#     fun2(n//2)
#     print(n % 2, end="")


# fun2(100)

print(100//2)
print(50//2)
print(25//2)
print(12//2)
print(6//2)
print(3//2)
print(1//2)

print()

print(0%2)
print(1%2)
print(3%2)
print(6%2)
print(12%2)
print(25%2)
print(50%2)
print(100%2)


# print(50%2)

# def f(x):
#     if x == 0:
#         return 0
#     else:
#         return 2 * f(x-1) + x * x
    


# fn = float(input("Enter a number: "))
# print("f(5) = ", f(fn))




# answer = f"The surface area of a cylinder with radius {radius:.2f} and height {height:.2f} is {calculation(radius, height):.2f}"
# print(answer)

import math


# def calculation(radius, height):
#     if radius < 0:
#         print("Please enter a positive number for radius")
#         exit()

#     if height < 0:
#         print("Please enter a positive number for radius")
#         exit()
    
#     return 2 * math.pi * radius * (radius + height)


radius = input("Enter radius:")
radius = float(radius)




if radius < 0:
    print("Please enter a positive number for radius")
    exit()


height = input("Enter height:")
height = float(height)

if height < 0:
    print("Please enter a positive number for radius")
    exit()

else:
    calculation = 2 * math.pi * radius * (radius + height)
    print(f"The surface area of a cylinder with radius {radius:.2f} and height {height:.2f} is {calculation:.2f}")







