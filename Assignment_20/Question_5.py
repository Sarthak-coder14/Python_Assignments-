import threading

def forward_print(start, end):
    print("Thread1 (Forward):")
    for i in range(start, end + 1):
        print(i)

def reverse_print(start, end):
    print("Thread2 (Reverse):")
    for i in range(end, start - 1, -1):
        print(i)

def main():
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    t1 = threading.Thread(
        target=forward_print,
        args=(start, end),
        name="Thread1"
    )

    t2 = threading.Thread(
        target=reverse_print,
        args=(start, end),
        name="Thread2"
    )

    t1.start()
    t1.join()     

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
