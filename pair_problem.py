


def solve1(A):
    # Find the maximum value in the list
    n = max(A)
    
    # Initialize the divisors list
    divisors = [0] * (n + 1)

    # Count divisors for each number up to n
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j] += 1

    # Calculate the result by summing up the divisor counts for each element in A
    res = 0
    for i in range(len(A)):
        res += divisors[A[i]]

    return res


def solve(A):
    import math
    
    max_val = max(A)
    count = 0
    for i in range(max_val + 1):
        for j in range(max_val + 1):
            if math.lcm(i, j) in A and math.gcd(i, j) in A:
                print(i, j)
                if i == j:
                    count += 2
                else:
                    count += 1
    return count

A = [3,6,7]
# A = [1,2,8]
print(solve1(A))
print(solve(A))
