def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print("Number of digits:")
    print(count)

def main():
    print("Enter number: ")
    num = int(input())
    count_digits(num)

if __name__ == "__main__":
    main()
