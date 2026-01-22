def numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")

def main():
    print("Enter number: ")
    num = int(input())
    numbers(num)

if __name__=="__main__":    

    main()
