from functools import reduce

def even_square_sum(lst):
    f = list(filter(lambda x: x % 2 == 0, lst))
    m = list(map(lambda x: x * x, f))
    r = reduce(lambda a, b: a + b, m)
    return f, m, r

def main():
    print("How many elements: ")
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    f, m, r = even_square_sum(numbers)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)

if __name__ == "__main__":
    main()
