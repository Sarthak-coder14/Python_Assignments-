import threading

def even_list(lst):
    even_sum = 0
    print("Even List:")
    for i in lst:
        if i % 2 == 0:
            print(i)
            even_sum += i
    print("Sum of even elements:", even_sum)

def odd_list(lst):
    odd_sum = 0
    print("Odd List:")
    for i in lst:
        if i % 2 != 0:
            print(i)
            odd_sum += i
    print("Sum of odd elements:", odd_sum)

def main():
    n = int(input("How many elements: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    t1 = threading.Thread(target=even_list, args=(numbers,))
    t2 = threading.Thread(target=odd_list, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threads completed")

if __name__ == "__main__":
    main()
