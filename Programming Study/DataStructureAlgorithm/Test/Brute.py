def string(T, P):
    n = len(T)
    m = len(P)

    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]:
            j += 1
        
        if j == m:
            return i
    return -1


def pack(wgt,val,W):
    n = len(wgt)
    bestVal = 0

    for i in range(2**n):
        s = [0]*n
        for d in range(n):
            s[d] = i%2
            i = i//2

        sumVal = 0
        sumWgt = 0

        for d in range(n):
            if s[d]== 1:
                sumVal += val[d]
                sumWgt += wgt[d]

        if sumWgt <= W:
            if sumVal > bestVal:
                bestVal = sumVal
    
    return bestVal