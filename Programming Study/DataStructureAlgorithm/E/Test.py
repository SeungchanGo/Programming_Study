# 1. 비닐하우스 자동 온도 제어
# while True:
#     x1 = int(input("온도를 입력: "))
#     if x1 < 25:
#         print("난방이 켜짐")
#     else:
#         print("난방이 꺼짐")   


# 2. 무인 주차장 설계
# while True:
#     x2 = input("자동차가 다가오면 1, 아니면 0: ")
#     if x2 == '1':
#         y2 = int(input('남은 주차공간 개수를 입력: '))
#         if y2 >= 1:
#             print("입차하세요")
#         else:
#             print("주차할 자기 없습니다.")   


# 3. 스마트 가로등
# while True:
#     x3 = int(input("빛의 밝기는? "))
#     if x3 <= 50:
#         y3 = int(input('자동차와의 거리? '))
#         if y3 <= 1:
#             print("가로등 켜기")
#         else:
#             print("가로등 끄기")

#     else:
#         print("가로등 끄기")                        


# 4. 이율 계산
# deMoney = int(input("예치 금액을 쓰세요. (만원 단위) >"))
# dePeriod = int(input("예치 개월을 쓰세요. >"))
# texfreeMoney = deMoney + deMoney * 0.02 * (dePeriod/12)
# print("예금 금리는 단리로 2%입니다.")
# print("비과세일 경우 집급앱은", texfreeMoney, "만원입니다.")


# # 5. 화장실 안내 프로그램
# empty = 5 # 빈자리
# use = 0 # 사용중
# print("빈자리: ", empty)
# print("사용중", use)

# def sensing():
#         global empty
#         global use
#         x5 = int(input("화장실을 사용한다: 1 / 화장실을 나온다: 2 >"))
#         if x5 == 1:
#             empty = empty -1
#             use = use + 1
#             print("빈자리: ", empty)
#             print("사용중", use)
#         else:
#             empty = empty + 1
#             use = use - 1 
#             print("빈자리: ", empty)
#             print("사용중", use)

# while True:
#     sensing()
#     if empty == 0:
#         print("빈자리가 없습니다. 잠시 기다려주시기 바랍니다.")
#     if empty == 5:
#         print("화장실이 모두 비었습니다.") 


# 6. 나무 그리기
import turtle


def drawTree(branch, t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15, t)
        t.left(40)
        drawTree(branch-15, t)
        t.right(20)
        t.backward(branch)

def main():
    t=turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)

main()    


# 음료주문하기
# person = 0
# coffee = 0
# icetea = 0
# latte = 0
# beverage = []
# person = int(input('몇명 인가요? '))
# for i in range(person):
#     order = input('아메리카노, 아이스티, 카페라떼 중에 고르시오. ')
#     beverage.append(order)

# for i in beverage:
#     if i == '아메리카노':
#         coffee += 1
#     elif i == '아이스티':
#         icetea += 1
#     else:
#         latte += 1

# print(f'아메리카노는 {coffee}잔입니다.')
# print(f'아이스티는 {icetea}잔입니다.')
# print(f'카페라뗴는 {latte}잔입니다.')

# person = 5
# icetea = 0
# coffee = 0
# juice = 0

# beverage = []
# for i in range(person):
#     order = input("icetea or coffee or juice? ")
#     beverage.append(order)

# for j in beverage:
#     if j == "coffee":
#         coffee += 1
#     elif j == "icetea":
#         icetea += 1
#     elif j == "juice":
#         juice += 1

# print(f"커피는 {coffee}잔 입니다.")
# print(f"아이스티는 {icetea}잔 입니다.")
# print(f"주스는 {juice}잔 입니다.")



# 점수의 합과 평균 구하기
# scores = [90, 90, 80, 50, 60]
# total = 0
# for i in range(len(scores)):
#     total = total + scores[i]
    
# average = total/len(scores)
# print("총점은", total,"입니다.")
# print("평균은",average,"입니다.")

# score = [90, 90, 80, 50, 60]
# total = 0
# for i in score:
#     total += i

# average = total / len(score)
# print(f"총점은 {total}입니다.")
# print(f'평균은 {average}입니다.')

# 키 큰 학생 찾기
# height = [176, 156, 166, 178, 182]
# temp = height[0]
# for i in range(len(height)-1):
#     if temp < height[i+1]:
#         temp = height[i+1]

# print("현재 가장 큰 값은", temp, "입니다.")        
# # print("내장함수를 이용한 가장 큰 값은", max(height), "입니다.")
# # print("내장함수를 이용한 가장 작은 값은", min(height), "입니다.")

# height = [176, 156, 166, 178, 182]
# temp = height[0]
# for i in range(0, len(height)-1):
#     if temp < height[i+1]:
#         temp = height[i+1]

# print("현재 가장 큰 값은", temp, "입니다.")       


# # 남녀 학생 수 세기
# attend = list('남여여남여여여남남남')
# man = 0
# woman = 0
# count = 0
# while count < len(attend):
#     if attend[count] == '남':
#         man += 1
#     else:
#         woman += 1
#     count += 1

# print("남자의 수는: ", man)
# print("여자의 수는: ", woman)    


# attend = list('남여여남여여여남남남')
# man = 0
# woman = 0

# for i in attend:
#     if i == "남":
#         man += 1
#     elif i == "여":
#         woman += 1

# print(f'남자는 {man}명 입니다.')
# print(f'여자는 {woman}명 입니다.')