def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def main():
    print("Enter number: ")
    num = int(input())
    if perfect(num):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()
