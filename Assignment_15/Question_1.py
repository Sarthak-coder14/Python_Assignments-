def square_list(nums):
    return list(map(lambda x: x*x, nums))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))
    print(square_list(nums))

if __name__ == "__main__":
    main()
