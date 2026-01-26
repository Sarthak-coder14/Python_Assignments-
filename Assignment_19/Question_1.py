power = lambda No : No ** 2

def main():
    Ret = 0
    print("Enter the number : ")
    Value = int(input())

    Ret = power(Value)
    print("Power is : ",Ret)
if __name__ == "__main__":
    main()
