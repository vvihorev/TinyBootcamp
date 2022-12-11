def two_sum_bool(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return True
    return False


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_all_pairs(nums, target):
    answer = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                answer.append([i, j])
    return answer


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_two_sum_bool():
    assert two_sum_bool(a, 15) == True
    assert two_sum_bool(a, 20) == False


def test_two_sum():
    assert two_sum(a, 7) in [[2, 3], [1, 4], [0, 5]]


def test_two_sum_all_pairs():
    assert two_sum_all_pairs(a, 7) == [[0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]


print(two_sum_all_pairs(a, 7))
