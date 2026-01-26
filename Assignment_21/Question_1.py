import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(lst):
    print("Prime Numbers:")
    for n in lst:
        if is_prime(n):
            print(n, end=" ")
    print()

def nonprime_numbers(lst):
    print("Non-Prime Numbers:")
    for n in lst:
        if not is_prime(n):
            print(n, end=" ")
    print()

def main():
    lst = list(map(int, input("Enter numbers separated by space: ").split()))

    t1 = threading.Thread(target=prime_numbers, args=(lst,))
    t2 = threading.Thread(target=nonprime_numbers, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
