def ChkGreater(no1, no2):
    if no1 > no2:
        
        print("Greater no is ",no1)
    else:
        print("Greater no is",no2)
def main():

    print("Enter First number :")
    value1=int(input())
    print("Enter Second number :")
    value2=int(input())

    ChkGreater(value1,value2)

if __name__=="__main__":
    main()