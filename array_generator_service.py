"""
https://leetcode.com/company/amazon/discuss/5429662/Amazon-OA
"""

def getNextState(state):
    return state | (state >> 1)  # Calculate the next state by shifting the current state right by 1 and OR'ing it with the current state

def getMaxAvailable(state, arr):
    # Determine the largest available element based on the current state
    N = len(arr)
    largest = float('-inf')
    position = 0
    while state > 0:
        if state & 1:
            # Calculate the offset from the rightmost bit
            # N-1-position gives the corresponding index in the array
            largest = max(largest, arr[N-1-position])
        state >>= 1  # Shift the state to the right to check the next bit
        position += 1  # Increment the position to track the offset
    return largest

def solution(arr, state, m):
    N = len(arr)
    state = int(state, 2)  # Convert state from binary string to integer
    res = []
    maxElement = max(arr)  # Find the maximum element in the array
    largest = getMaxAvailable(state, arr)  # Get the largest available element based on the initial state
    stateCanBeUpdated = maxElement != largest  # Flag to determine if state updates are necessary

    while m:
        # Append the largest available element to the result list
        res.append(largest)

        if stateCanBeUpdated:
            nextState = getNextState(state)  # Calculate the next state
            diff = nextState ^ state  # Determine the difference from the current state

            if not diff:
                stateCanBeUpdated = False  # If no new elements are available, stop updating the state
            else:
                largest = max(largest, getMaxAvailable(diff, arr))  # Update the largest available element
                state = nextState  # Update the state
                if largest == maxElement:
                    stateCanBeUpdated = False  # If the largest available element is the maximum element, stop updating the state
        m -= 1

    return res


def solve(arr, states, m):
    S = []
    curr_max = float('-inf')
    i = 0
    to_flip = [0] * m
    while i < len(arr):
        if states[i] == '1':
            curr_max = max(curr_max, arr[i])
            i += 1
        else:
            count = 0
            while i < len(arr) and states[i] == '0':
                # check `curr_max > 0` to avoid flipping leading zeros
                if curr_max > 0 and count + 1 < m:
                    to_flip[count + 1] = max(to_flip[count], arr[i])
                    count += 1
                i += 1
                
    
    curr = curr_max
    for i in range(m):
        if to_flip[i] > curr:
            curr = to_flip[i]
        S.append(curr)
    
    return S


arr = [10,1,2,1,1,2,4,5,7,8,9,10,11,12]
state = "00110111000000"
m = 5

import timeit
print(timeit.timeit("solution(arr, state, m)", globals=globals(), number=1000))
print(timeit.timeit("solve(arr, state, m)", globals=globals(), number=1000))
