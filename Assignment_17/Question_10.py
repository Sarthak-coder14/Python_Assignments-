def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print("Addition of digits:")
    print(total)

def main():
    print("Enter number: ")
    num = int(input())
    sum_of_digits(num)

if __name__ == "__main__":
    main()
