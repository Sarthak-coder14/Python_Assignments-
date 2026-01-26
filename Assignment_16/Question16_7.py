def divisibleByFive(n):
    return n % 5 == 0

def main():
    print("Enter number: ")
    n = int(input())
    print(divisibleByFive(n))

if __name__ == "__main__":
    main()
