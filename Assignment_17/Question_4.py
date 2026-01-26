def sumOfFactors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total = total + i
    return total

def main():
    print("Enter number: ")
    n = int(input())
    print("Addition of factors:", sumOfFactors(n))

if __name__ == "__main__":
    main()
