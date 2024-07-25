fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(8)]
print(" ".join(map(str, fibonacci)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# fibonacci = [0, 1]
# [fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(8)]
# print(fibonacci)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
