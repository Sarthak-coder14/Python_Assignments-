def DisplayGrade(No):
    if(No >= 75 and No <= 100):
        print("You are pass with Distinction")
    elif(No >= 60 and No < 75):
        print("You are pass with First Class")
    elif(No >= 50 and No < 60):
        print("You are pass with Second Class")
    elif(No > 1 and No < 50):
        print("Sorry you are Fail,Try next time")
    else:
        print("Enter Valid marks")

def main():

    print("Enter Your Marks : ")
    Marks = int(input())

    DisplayGrade(Marks)
    
if __name__ == "__main__":
    main()