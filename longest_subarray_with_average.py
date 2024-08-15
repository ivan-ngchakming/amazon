"""
I have an array of size n and am given an integer limit k. 
I have to return the maximum length of a subarray 
where each element in that subarray exceeds the value of (k / length of that subarray)


Notes:
k / n gets smaller for larger n
starts with largest subarray and shrinks
we want all elements to be greater than k / n
remove the smaller one from the edges
"""
from heapq import heappush, heappop, heapify


def solve0(arr, k):
    def is_valid(arr, k):
        return all(x > k / len(arr) for x in arr)
    res = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
           if is_valid(arr[i:j+1], k):
               res = max(res, j - i + 1)
    return res


def solve(arr, k):
    min_val, min_index = min([(val, i) for i, val in enumerate(arr)], key=lambda x: x[0])
    if min_val > k / len(arr):
        return len(arr)
    return max(
        # left subarray
        solve(arr[:min_index], k) if min_index > 0 else 0,
        solve(arr[min_index+1:], k) if min_index < len(arr) - 2 else 0
    )


test_cases = [
    ([5, 7, 10, 4], 10, 4),
    ([20], 10, 1),
    ([2, 2, 2, 2], 10, 0),
    ([15, 15, 15], 10, 3),
    ([1, 10, 5, 12, 4], 20, 0),
    ([100, 200, 300, 400], 1000, 0),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 10),
    ([2, 3, 4, 10, 12, 15, 1, 3], 10, 6),
    ([8, 54, 94, 27, 20, 14, 53, 10, 24, 29, 89, 52, 5, 64, 31, 35, 29, 40, 43, 47], 144, 7)
]


for arr, k, expected in test_cases:
    print(f"arr = {arr}; k = {k}; expected = {expected}")
    assert solve0(arr, k) == expected, f"expected = {expected}, got = {solve0(arr, k)}"
    assert solve(arr, k) == expected, f"expected = {expected}, got = {solve(arr, k)}"

import random
for i in range(100):
    arr = [random.randint(1, 100) for _ in range(random.randint(1, 100))]
    k = random.randint(1, 200)
    assert solve(arr, k) == solve0(arr, k), f"arr = {arr}; k = {k}; solve = {solve(arr, k)}, solve0 = {solve0(arr, k)}"
