def divisible_3_5(nums):
    return list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(divisible_3_5(nums))

if __name__ == "__main__":
    main()
