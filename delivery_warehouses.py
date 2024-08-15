def solve(centers: list[int], d: int) -> int:
    if not centers:
        return 0
    
    left_bound = float('-inf')
    right_bound = float('inf')
    for center in centers:
        left_bound = max(left_bound, center - d)
        right_bound = min(right_bound, center + d)
    
    # assuming center and warehouse can be in the same location
    if right_bound >= left_bound:
        return right_bound - left_bound + 1
    else:
        return 0

if __name__ == "__main__":
    assert solve([1, 5, 9], 4) == 1
    assert solve([1], 2) == 5
    assert solve([], 100) == 0
    assert solve([1, 10], 2) == 0
