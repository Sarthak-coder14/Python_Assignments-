def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 == 0 ,Data))

    print("Even number is :",Fdata)

if __name__ == "__main__":
    main()