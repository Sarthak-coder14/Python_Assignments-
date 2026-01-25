def main():
    Sum = 0
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda No : No % 2 == 0 ,Data))

    for i in range(len(Fdata)):
        Sum = Sum + 1
    
    print("Even number count is :",Sum)

if __name__ == "__main__":
    main()