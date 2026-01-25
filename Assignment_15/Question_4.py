from functools import reduce

def sum_numbers(nums):
    return reduce(lambda x, y: x + y, nums)

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(sum_numbers(nums))

if __name__ == "__main__":
    main()
