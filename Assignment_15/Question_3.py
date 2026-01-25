def odd_numbers(nums):
    return list(filter(lambda x: x % 2 != 0, nums))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(odd_numbers(nums))

if __name__ == "__main__":
    main()
