def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    print("Enter number: ")
    n = int(input())
    print("Factorial:", factorial(n))

if __name__ == "__main__":
    main()
