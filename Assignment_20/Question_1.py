import threading

def even_numbers():
    print("Even Thread:")
    for i in range(2, 21, 2):
        print(i)

def odd_numbers():
    print("Odd Thread:")
    for i in range(1, 20, 2):
        print(i)

def main():
    t1 = threading.Thread(target=even_numbers)
    t2 = threading.Thread(target=odd_numbers)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
