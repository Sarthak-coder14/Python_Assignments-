largest = lambda a, b, c: a if a > b and a > c else (b if b > c else c)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Largest Number is :", largest(a, b, c))

if __name__ == "__main__":
    main()
