from func_test_utils import timeit, read_list_of_integers


@timeit
def find_max_module_linear(nums):
    min = max = nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    return max - min


@timeit
def find_min_module_brute(nums):
    min = nums[1] - nums[0]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] - nums[j] < min:
                min = nums[i] - nums[j]
    return min


@timeit
def find_min_module_sorted(nums):
    nums.sort()
    min = nums[-1] - nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i] - nums[i - 1] < min:
            min = nums[i] - nums[i - 1]
    return min


for test_input in ['input-100.txt', 'input-1000.txt', 'input-10000.txt']:
    print(f'Current input file: `{test_input}`')
    nums = read_list_of_integers(test_input)
    find_max_module_linear(nums)
    find_min_module_brute(nums)
    find_min_module_sorted(nums)
    print()

