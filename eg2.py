def listReversed(myList,a, n):
    if a >= n:
        return
    myList[a], myList[n] = myList[n], myList[a]
    print(listReversed(myList, a+1, n-1))
    
    

try:
    n = int(input("Enter n: "))
    my_list = input(f"Enter {n} integers: ").split()
    # my_list = list(map(int, my_list))
    print("Original list: "+ ' '.join(map(str, my_list)))
    print("Start reversing ...")
    listReversed(my_list,0, n-1)
except IndexError as e:
    print(f"Error: {e}")

# print(' '.join(map(str, my_list)))