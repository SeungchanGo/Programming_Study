# 예외 처리
#f = open("나없는 파일", r)
#print(4 / 0)


#오류 예외 처리 기법
#1. try, except문
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)    

#2. try...fianlly
f = open('foo.txt', 'w')
try:
   print("x")
finally:
    f.close()

#3. 여러 개의 오류 처리하기
#try:
    #a = [1.2]
    #print(a[3])
    #4/0
#except ZeroDivisionError:
    #print("0으로 나눌 수 없습니다.")
#except IndexError:
    #print("인덱싱할 수 없습니다.")

try:
    a = [1.2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
    

#오류 회피하기
try:
    f = open("나 없는 파일", 'r')
except FileNotFoundError:
    pass


#오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError # Bird 클래스를 상속받는 자식 클래스는 반드시 fly함수를 구현해야 함을 의미
    
#class Eagle(Bird):
#    pass

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


#예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사") 
    say_nick("바보")   
except MyError:
    print("허용되지 않는 별명입니다.")