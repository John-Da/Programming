import math


a = float(input("Digit: "))
power = float(input("multiplier: "))
b = math.pow(10, power)
meter = float(input("meter: "))

plus = a * b
erro = ((plus - meter) / plus) * 100

# if int(meter) > int(plus):
#     new_erro = 100 - erro
# elif int(meter) < int(plus):
#     new_erro = erro
# else:
#     print("none")

print(f"Pos: {plus}")
print(f"% {abs(erro)}")