A = [7, 2, 4, 1, 3, 6, 5, 0]


def insert_sort(A):
    A_sorted = []
    for i in range(len(A)):
        min = A[0]
        min_index = 0
        for i in range(len(A)):
            if A[i] < min:
                min = A[i]
                min_index = i
        A.pop(min_index)
        A_sorted.append(min)
    return A_sorted


print(insert_sort(A))

