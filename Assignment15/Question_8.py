def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : (No % 3 == 0) and (No % 5 == 0),Data))

    print("The number which divisible by 3 and 5 are :",Fdata)

if __name__ == "__main__":
    main()