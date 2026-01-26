from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_max(lst):
    f = list(filter(lambda x: is_prime(x), lst))
    m = list(map(lambda x: x * 2, f))
    r = reduce(lambda a, b: a if a > b else b, m)
    return f, m, r

def main():
    print("How many elements: ")
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    f, m, r = prime_max(numbers)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)

if __name__ == "__main__":
    main()
