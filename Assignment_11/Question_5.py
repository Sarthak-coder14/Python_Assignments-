def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return temp == rev

def main():
    print("Enter number: ")
    num = int(input())
    if  palindrome(num):
        print("Palindrome")
    else:
        print("Not Palindrome")

main()
