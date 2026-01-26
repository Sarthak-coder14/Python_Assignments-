def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j)
        print()

def main():
    num = int(input("Enter number: "))
    pattern(num)

if __name__ == "__main__":
    main()
