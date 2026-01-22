def digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def main():
    print("Enter number: ")
    num = int(input())
    print(digits(num))

main()
