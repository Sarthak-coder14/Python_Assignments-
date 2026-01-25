def count_even(nums):
    return len(list(filter(lambda x: x % 2 == 0, nums)))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(count_even(nums))

if __name__ == "__main__":
    main()
