import time


def two_sum_bool(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return True
    return False


def two_sum(nums, target):
    residuals = {}
    for i in range(len(nums)):
        res= target - i
        if res in residuals:
            return [residuals[res], i]
        else:
            residuals[res] = i
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
    assert two_sum_bool(a, 15)
    assert not two_sum_bool(a, 20)


def test_two_sum():
    assert two_sum(a, 7) in [[2, 3], [1, 4], [0, 5]]


def test_two_sum_all_pairs():
    assert two_sum_all_pairs(a, 7) == [[0, 5], [1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]


for i in range(0, 4):
    start = time.time()
    two_sum(a*10**i, 7)
    print(f"10**{i}:\t{(time.time() - start):.5f}")
