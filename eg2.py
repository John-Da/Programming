first_num = float(input("Enter a number"))
second_num = float(input("Enter a number"))
total_num = first_num + second_num
print(f"{first_num:.1f} + {second_num:.1f} = {total_num:.1f}")

print("Writing to file numbers.txt")

with open("numbers.txt", "w" ) as test:
    test = test.write(f"{first_num:.1f} + {second_num:.1f} = {total_num:.1f}")

print("Reading from file numbers.txt")

with open("numbers.txt", "r" ) as test:
    print(test.read())