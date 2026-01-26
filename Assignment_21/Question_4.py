import threading

def calc_sum(lst, result):
    result['sum'] = sum(lst)

def calc_product(lst, result):
    prod = 1
    for i in lst:
        prod *= i
    result['product'] = prod

def main():
    lst = list(map(int, input("Enter numbers: ").split()))
    result = {}

    t1 = threading.Thread(target=calc_sum, args=(lst, result))
    t2 = threading.Thread(target=calc_product, args=(lst, result))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum:", result['sum'])
    print("Product:", result['product'])

if __name__ == "__main__":
    main()
