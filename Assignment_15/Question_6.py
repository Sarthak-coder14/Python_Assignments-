from functools import reduce

def min_number(nums):
    return reduce(lambda x, y: x if x < y else y, nums)

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(min_number(nums))

if __name__ == "__main__":
    main()
