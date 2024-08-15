"""
https://leetcode.com/company/amazon/discuss/5623532/Amazon-or-OA-or-2024
"""

import math
def solve(parcels: list[int], extra_parcels: int):
    max_agent = max(parcels)
    for parcel in parcels:
        extra_parcels -= max_agent - parcel
    if extra_parcels <= 0:
        return max_agent
    
    return math.ceil(extra_parcels / len(parcels)) + max_agent

print(solve([7,5,1,9,1], 25))
print(solve([7,5,1,9,1], 1))
