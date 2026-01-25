div5 = lambda x: x % 5 == 0

def main():
    n = int(input("Enter number: "))
    print("Divisible by 5:", div5(n))

if __name__ == "__main__":
    main()
