def max_points_from_tournament_tasks__example(days, k):
    total_days = sum(days)

    # Tournaments can loop around, so we need to double the combined days
    combined_days = []
    for _ in range(2):
        for day in days:
            combined_days.extend(range(1, day + 1))

    # Fixed size sliding window
    l, r = 0, 0
    max_points = float('-inf')
    curr_points = 0

    while r < len(combined_days):
        curr_points += combined_days[r]
        while r - l + 1 > k:
            curr_points -= combined_days[l]
            l += 1
        max_points = max(max_points, curr_points)
        r += 1

    return max_points if max_points != float('-inf') else 0

def max_points_from_tournament_tasks(days: list[int], k: int) -> int:
    score = [i for d in days for i in range(1, d + 1)]
    score.extend(score[:k])
    
    curr = sum(score[:k])
    max = curr
    pointer = 0
    while pointer + k < len(score):
        curr -= score[pointer]
        curr += score[pointer + k]
        pointer += 1
        if curr > max:
            max = curr
    return max

k = 4
days = [3, 1, 1, 1, 1, 1, 1, 3]
print(max_points_from_tournament_tasks__example(days, k))
print(max_points_from_tournament_tasks(days, k))
