from functools import reduce

def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    print("The data is : ",Data)

    Fdata = int(reduce(lambda a, b: (a < b) and a or b,Data))

    print(Fdata)


if __name__ == "__main__":
    main()