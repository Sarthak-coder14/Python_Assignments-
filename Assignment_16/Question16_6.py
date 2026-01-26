def checkNumber(n):
    if n > 0:
        print("Positive Number")
    elif n < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    n = int(input("Enter number: "))
    checkNumber(n)

if __name__ == "__main__":
    main()
