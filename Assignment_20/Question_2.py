import threading

def even_factor(n):
    sum_even = 0
    print("Even Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            print(i)
            sum_even += i
    print("Sum of even factors:", sum_even)

def odd_factor(n):
    sum_odd = 0
    print("Odd Factors:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            print(i)
            sum_odd += i
    print("Sum of odd factors:", sum_odd)

def main():
    num = int(input("Enter number: "))

    t1 = threading.Thread(target=even_factor, args=(num,))
    t2 = threading.Thread(target=odd_factor, args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
