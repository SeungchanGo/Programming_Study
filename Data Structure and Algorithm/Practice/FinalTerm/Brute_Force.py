def string_matching(T, P):
    n = len(T)
    m = len(P)

    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]:
            j = j+1
        if j == m:
            return i
    return -1

print(string_matching('HELLOW WORLD', 'LO'))



def Knapsack01_BF(wgt, val, W): #wgt: 물건들의 무게 리스트, val: 물건들의 가치 리스트, W: 배낭의 무게
    n = len(wgt) 
    bestVal = 0 # 배낭의 최대 가치

    for i in range(2**n): 
        s = [0] * n
        for d in range(n): # 이진수 만들기
            s[d] = i%2
            i = i//2 # 0 => [0,0,0], 1 => [1,0,0]

        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]

        if sumWgt <= W:
            if sumVal > bestVal:
                bestVal = sumVal
    
    return bestVal

weight = [10, 20, 30, 25, 35]
value = [60, 100, 120, 70, 85]
W = 80
bestV = Knapsack01_BF(weight, value, W)
print("배낭채우기 문제(억지기법) 최대용량:", bestV)