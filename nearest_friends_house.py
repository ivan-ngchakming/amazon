"""
https://leetcode.com/discuss/interview-question/5360203/Amazon-OA
"""

def solve_example(locations):
    n = len(locations)
    pref_sum = [0] * n
    
    # Sort the locations
    locations.sort()
    
    # Calculate the prefix sum
    pref_sum[0] = locations[0]
    for i in range(1, n):
        pref_sum[i] = pref_sum[i - 1] + locations[i]
    
    ans = [0] * n
    
    for i in range(n):
        if i == 0:
            distance = pref_sum[n - 2] - pref_sum[0]
            distance -= locations[i] * (n - 2)
        elif i == n - 1:
            distance = pref_sum[n - 2] - pref_sum[0]
            distance -= locations[i] * (n - 2)
            distance *= -1
        else:
            diff1 = locations[i] - locations[0]
            diff2 = locations[n - 1] - locations[i]

            # Compare which one friend is closer
            if diff1 >= diff2:
                distance = pref_sum[n - 1] - pref_sum[i]
                distance -= locations[i] * (n - i - 1)
                d = pref_sum[i - 1] - pref_sum[0]
                d -= locations[i] * (i - 1)
                d *= -1
                distance += d
            else:
                distance = pref_sum[n - 2] - pref_sum[i]
                distance -= locations[i] * (n - i - 2)
                d = pref_sum[i - 1]
                d -= locations[i] * i
                d *= -1
                distance += d
        
        ans[i] = distance
    
    return ans

def solve(locations):
    """
    Brute force solution
    """
    distances = [[] for _ in locations]
    for friend in locations:
        for i, house in enumerate(locations):
            if friend != house:
                distances[i].append(abs(friend - house))
    return [sum(sorted(d)[:-1]) for d in distances]

def solve__optimized(locations):
    if len(locations) == 1:
        return [0]

    prefix_sum = [sum(locations[:i]) for i in range(1, len(locations) + 1)]
    n = len(locations)
    res = []
    for i, location in enumerate(locations):
        if i == 0 or i == n - 1:
            distance = abs(location * (n - 2) - (prefix_sum[-2] - prefix_sum[0]))
        else:
            first_house_distance = locations[0] - location
            last_house_distance = abs(locations[-1] - location)
            if first_house_distance < last_house_distance:
                # first house is closer
                left_distance = location * i - prefix_sum[i-1]
                right_distance = location * (n-2-i) - (prefix_sum[-2] - prefix_sum[i])
                distance = left_distance - right_distance
            else:
                # last house is closer
                left_distance = location * (i-1) - (prefix_sum[i-1] - prefix_sum[0])
                right_distance = location * (n-i-1) - (prefix_sum[-1] - prefix_sum[i])
                distance = left_distance - right_distance
        res.append(distance)
    return res

locations = [2,3,5,7,9,12,13,14,15,18,20,22,25,30,37,40,45,50,55,60,70,80,90,100]
print(solve_example(locations))
print(solve(locations))
print(solve__optimized(locations))

import timeit

number = 10000
print(timeit.timeit("solve_example(locations)", globals=globals(), number=number))
print(timeit.timeit("solve(locations)", globals=globals(), number=number))
print(timeit.timeit("solve__optimized(locations)", globals=globals(), number=number))
