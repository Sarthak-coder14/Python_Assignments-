def Min(Arr):
    temp = Arr[0]
    for i in range(1,len(Arr)):
        if(temp > Arr[i]):
            temp = Arr[i]       
    return temp


def main():
    print("number of elements : ")
    Size = int(input())

    Data = []

    print("List of number is : ")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print(Data)

    Ret = Min(Data)

    print("Maximum number is : ",Ret)
if __name__ == "__main__":
    main()
