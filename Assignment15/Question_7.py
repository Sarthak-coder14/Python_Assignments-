def main():
    print("Enter the element count :")
    Size = int(input())

    Data = []

    print("Enter the elements:")
    for i in range(Size):
        value = str(input())
        Data.append(value)
    print("The Actual data is : ",Data)

    Fdata = list(filter(lambda a : len(a) > 5 ,Data))

    print(Fdata)

    if(len(Fdata) >= 0):
        print("There is no String having lenght is grater than or equal 5")
       


if __name__ == "__main__":
    main()