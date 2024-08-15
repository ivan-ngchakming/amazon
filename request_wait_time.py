from sortedcontainers import SortedList

def solve0(requests, waitTime):    
    result = []
    currTime = 0
    remainingRequests = SortedList((wait_time[i], i) for i in range(requests))
    indexes = set()
    id = 0
    while remainingRequests:
        result.append(len(remainingRequests))
        if currTime not in indexes:
            idx = remainingRequests.bisect_left((waitTime[currTime], currTime))
            indexes.add(currTime)
            remainingRequests.pop(idx)
        # else:
        #     while currTime in indexes:
        #         currTime += 1
        currTime += 1
        while remainingRequests and remainingRequests[0][0] <= currTime:
            indexes.add(remainingRequests[0][1])
            remainingRequests.pop(0)
    while currTime < requests:
        currTime += 1
        result.append(0)
    return result


def solve(wait_time):
    res = [len(wait_time)]

    for i in range(1, len(wait_time)):
        for j in range(i, len(wait_time)):
            wait_time[j] -= 1
        active = sum(1 for t in wait_time[i:] if t > 0)
        if active == 0:
            return res
        res.append(active)
    return res

def solve2(wait_times):
    n = len(wait_times)
    active = [i for i in range(n, 0, -1)]
    
    for i, wait_time in enumerate(wait_times):
        if wait_time <= i:
            for j in range(wait_time, i+1):
                active[j] -= 1
    while active and active[-1] == 0:
        active.pop()
    return active

wait_time = [5,2,1,1,1,4]
print(solve0(len(wait_time), wait_time.copy())) # [6,4,2,2,1]
print(solve(wait_time.copy())) # [6,4,2,2,1]
print(solve2(wait_time.copy())) # [6,4,2,2,1]
