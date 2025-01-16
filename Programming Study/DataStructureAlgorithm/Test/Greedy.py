def Pack(wgt, val, W):
    bestVal = 0

    for i in range(len(wgt)):
        if W <= 0:
            break
        if W >= wgt[i]:
            W -= wgt[i]
            bestVal += val[i]
        
        else:
            fraction = W/wgt[i]
            bestVal += fraction * val[i]
            break

    return bestVal