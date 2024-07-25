import math


def Euclidean(x1, y1, x2, y2):
    return f"{math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2)):.4f}"


def Manhattan(x1, y1, x2, y2):
    return f"{abs(x1-x2) + abs(y1-y2):.4f}"


def main():
    while True:
        try:
            x1, y1, x2, y2 = map(int, input("Enter x1, y1, x2, y2: ").split())
            manhattan = Manhattan(x1, y1, x2, y2)
            euclidean = Euclidean(x1, y1, x2, y2)
            print("Manhattan distance = ", manhattan)
            print("Euclidean distance = ", euclidean)
            exit()
        except (ValueError, IndexError):
            print("Something wrong")


if __name__ == "__main__":
    main()
