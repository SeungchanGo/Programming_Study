#for문

#1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#3. for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


#4. for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생은 합격입니다. 축하합니다." % number)       


#5. for문과 함께 자주 사용하는 range 함수
a = range(10) # 0,1,2,3,4,5,6,7,8,9
print(a) 
a = range(1, 11) #1,2,3,4,5,6,7,8,9,10

add = 0
for i in range(1, 11):
    add = add + i
print(add)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('') 


#6. 리스트 내포 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3) #result = [3,6,9,12]
print(result)

result = [num * 3 for num in a]
print(result)

