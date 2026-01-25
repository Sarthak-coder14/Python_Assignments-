from functools import reduce

def max_number(nums):
    return reduce(lambda x, y: x if x > y else y, nums)

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(max_number(nums))

if __name__ == "__main__":
    main()
