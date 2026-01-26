def chkNum(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter number: ")
    n = int(input())
    chkNum(n)

if __name__ == "__main__":
    main()
