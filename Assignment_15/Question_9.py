from functools import reduce

def product_numbers(nums):
    return reduce(lambda x, y: x * y, nums)

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(product_numbers(nums))

if __name__ == "__main__":
    main()
