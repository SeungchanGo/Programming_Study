def KnapSackFrac(wgt, val, W):
    bestVal = 0 # 최대 가치
    for i in range(len(wgt)): # 단가가 높은 물건부터 처리
        if W <= 0: # 용량이 다 찼으면 채우기 종료
            break

        # 물건 전체를 넣을 수 있으면 넣고, 남은 용량 W를 갱신    
        if W >= wgt[i]: 
            W -= wgt[i]
            bestVal += val[i]

        # 일부만 넣을 수 있으면, 최대 비율을 계산하고, 최대한 채움.
        else:
            fraction = W/wgt[i]
            bestVal += val[i] * fraction
            break

    return bestVal # 최대 가치 반환

weight = [12, 10, 8]
value = [120, 80, 60]
W = 18
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W))

weight = [10, 20, 30]
value = [60, 100, 120]
W = 50
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W))
