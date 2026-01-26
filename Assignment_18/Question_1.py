def Sum(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum


def main():
    print("number of elements : ")
    Size = int(input())

    Data = []

    print("List of number is : ")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print(Data)

    Ret = Sum(Data)

    print("Sum of all elements are : ",Ret)
if __name__ == "__main__":
    main()
