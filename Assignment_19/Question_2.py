Mul = lambda No1 , No2 : No1 * No2

def main():
    Ret = 0
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())


    Ret = Mul(Value1,Value2)
    print("Multiplication is : ",Ret)
if __name__ == "__main__":
    main()
