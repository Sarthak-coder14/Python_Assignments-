def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

def main():
    print("Enter Number")

    No = int(input())

    factorial(No)

if __name__ == "__main__":
    main()
