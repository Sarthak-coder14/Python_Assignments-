def Divisible(no):
    if  (no % 3 == 0) & (no % 5 == 0):

        print("Divisible by 3 & 5 ")
    else:
        print("not divisible by 3 & 5 ")

    

def main():

    print("Enter Number : ")
    No = int(input())

    Ret = Divisible(No)

    
if __name__ == "__main__":
    main()






