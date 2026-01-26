def Count(Arr,No):
    Count = 0
    for i in range(len(Arr)):
        if(Arr[i] == No):
            Count = Count + 1
                  
    return Count


def main():
    print("number of elements : ")
    Size = int(input())

    Data = []

    print("List of number is : ")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print(Data)

    print("Elemet to search")
    Value = int(input())

    Ret = Count(Data,Value)

    print("Frequency is : ",Ret)
if __name__ == "__main__":
    main()
