def find_zero_intervals(s):
    zeros = []
    start = None
    
    for i, char in enumerate(s):
        if char == '0':
            if start is None:
                start = i
        elif start is not None:
            zeros.append((start, i - 1))
            start = None
    
    if start is not None:
        zeros.append((start, len(s) - 1))
    
    return zeros


def solve(k, switches):
    zeros = find_zero_intervals(switches)
    
    # check for edge case where there are less than k sets of zeros
    # in this case we can just flip all of them
    if len(zeros) <= k:
        return len(switches)
    
    # set initial max_flipped to the number of 
    # flipping the first k sets of zeros
    max_flipped = max(0, zeros[k][0])
    
    # iteratively checking the next k sets of zeros
    for i in range(k, len(zeros)):
        start = zeros[i - k][1] + 1
        
        if i == len(zeros) - 1:
            end = len(switches) - 1  
        else:
            end = zeros[i + 1][0] - 1
        curr_flipped = end - start + 1
        max_flipped = max(max_flipped, curr_flipped)
    
    return max_flipped

if __name__ == '__main__':
    print(solve(1, '00010'))
    print(solve(2, '11101010110011'))
