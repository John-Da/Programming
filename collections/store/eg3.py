def reverse_list(arr):

    if len(arr) <= 1:
        return
    
    arr[0], arr[-1] = arr[-1], arr[0]
    
    reverse_list(arr[1:-1])


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Enter {n} integers:", end=" ")
    arr = list(map(int, input().split()))
    
    print("Original list:", " ".join(map(str, arr)))
    
    print("Start reversing ...")
    reverse_list(arr)
    
    print("Reversed list:", " ".join(map(str, arr)))
