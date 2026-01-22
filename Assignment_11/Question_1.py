def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    print("Enter Number")
    num = int(input())
    if prime(num):
        print("Prime Number")
    else:
        print("Not Prime Number")

main()
