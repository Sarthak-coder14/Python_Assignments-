def print_reverse(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

def main():
    print("Enter number: ")
    num = int(input())
    print_reverse(num)
    
if __name__=="__main__":

    main()
