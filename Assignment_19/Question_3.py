from functools import reduce

def process_numbers(lst):
    f = list(filter(lambda x: x >= 70 and x <= 90, lst))
    m = list(map(lambda x: x + 10, f))
    r = reduce(lambda a, b: a * b, m)
    return f, m, r

def main():
    print("How many elements: ")
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    f, m, r = process_numbers(numbers)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)

if __name__ == "__main__":
    main()
