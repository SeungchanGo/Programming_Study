from collections import deque

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]
    
def solution2(numbers, direction):
    dq = deque(numbers)
    if direction == "right":
        dq.rotate(1)
    else:
        dq.rotate(-1)    
    return list(dq)

numbers = [1, 2, 3]
result = solution2(numbers, "right")
print(result)
result = solution2(numbers, "left")    
print(result)