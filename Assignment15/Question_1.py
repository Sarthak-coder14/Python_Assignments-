def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Mdata = list(map(lambda Arr : Arr * Arr,Data))

    print("Suqare of each elements is :",Mdata)

if __name__ == "__main__":
    main()