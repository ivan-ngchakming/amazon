def solve0(products, k):
    def score(arr):
        res = 1
        for j in range(len(arr)-1, 0, -1):
            if arr[j-1] > arr[j]:
                res += 1
            else:
                return res
        return res
    
    res = 0
    for i in range(len(products)-k+1):
        s = score(products[i:i+k])
        print(products[i:i+k], s)
        res += s
    return res

products = [1,2,3,4]
print(solve0(products, 3))