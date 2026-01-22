def BinaryForm(No):
    Binary = None
    Data = []

    while(No != 0):
        Binary = No % 2
        Data.append(Binary)
        No = No // 2
    return Data
   

def main():
    Ret = 0
    print("Enter number : ")
    Value = int(input())

    Ret = BinaryForm(Value)
    
    print(Ret)

    
if __name__ == "__main__":
    main()