def firstEvenNumbers(n):
    result = ""
    for i in range(1, n + 1):
        result = result + str(i * 2) + " "
    print(result)

def main():
    print("Enter how many even numbers: ")
    n = int(input())
    firstEvenNumbers(n)

if __name__ == "__main__":
    main()
