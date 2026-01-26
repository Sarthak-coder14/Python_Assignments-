import threading

counter = 0
lock = threading.Lock()

def increment(count):
    global counter
    for _ in range(count):
        with lock:
            counter += 1

def main():
    print("Enter number of increments per thread: ")
    n = int(input())

    t1 = threading.Thread(target=increment, args=(n,))
    t2 = threading.Thread(target=increment, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter Value:", counter)

if __name__ == "__main__":
    main()
