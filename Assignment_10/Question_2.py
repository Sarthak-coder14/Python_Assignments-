def sum(n):
    ANS = 0
    for i in range(1, n + 1):
        ANS += i
    print(ANS)

def main():
    print("Enter number")
    No = int(input())

    sum(No)

if __name__ == "__main__":
    main()

