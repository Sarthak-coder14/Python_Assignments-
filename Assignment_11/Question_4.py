def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev

def main():
    print("Enter number: ")
    no = int(input())
    print("reverse is :",reverse(no))
   

main()
