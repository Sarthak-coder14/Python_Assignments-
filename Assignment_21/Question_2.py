import threading

def find_max(lst):
    print("Maximum:", max(lst))

def find_min(lst):
    print("Minimum:", min(lst))

def main():
    lst = list(map(int, input("Enter list elements: ").split()))

    t1 = threading.Thread(target=find_max, args=(lst,))
    t2 = threading.Thread(target=find_min, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
