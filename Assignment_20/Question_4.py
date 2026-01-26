import threading

def small_letters(s):
    count = 0
    t = threading.current_thread()
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread ID:", t.ident)
    print("Thread Name:", t.name)
    print("Lowercase count:", count)
    print()

def capital_letters(s):
    count = 0
    t = threading.current_thread()
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread ID:", t.ident)
    print("Thread Name:", t.name)
    print("Uppercase count:", count)
    print()

def digit_count(s):
    count = 0
    t = threading.current_thread()
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread ID:", t.ident)
    print("Thread Name:", t.name)
    print("Digit count:", count)
    print()

def main():
    text = input("Enter string: ")

    t1 = threading.Thread(target=small_letters, args=(text,), name="Small")
    t2 = threading.Thread(target=capital_letters, args=(text,), name="Capital")
    t3 = threading.Thread(target=digit_count, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
