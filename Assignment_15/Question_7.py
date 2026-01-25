def long_strings(words):
    return list(filter(lambda s: len(s) > 5, words))

def main():
    words = input("Enter strings: ").split()
    print(long_strings(words))

if __name__ == "__main__":
    main()
