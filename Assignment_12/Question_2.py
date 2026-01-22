def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

def main():
    print("Enter number: ")
    num = int(input())
    factors(num)

if __name__=="__main__":
    main()
