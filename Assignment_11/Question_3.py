def sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def main():
    print("Enter number: ")
    num = int(input())
    print(sum(num))

main()
