#클래스
class Cookie:
    pass
a = Cookie()
b = Cookie()


#1. 사칙연산 클래스
class FourCal:

    #생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second

    #1) 객체에 숫자 저장
    def setdata(self, first, second): #self는 setdata를 호출하는 객체가 대입되는 변수이다.
        self.first = first
        self.second = second   

    #2) 더하기 기능   
    def add(self):
        result = self.first + self.second
        return result 
    
    #3) 빼기 기능
    def sub(self):
        result = self.first + self.second
        return result
    
    #4) 곱하기 기능
    def mul(self):
        result = self.first * self.second
        return result
    
    #5) 나누기 기능
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(3,4)
print(a.add())
a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add()) 
print(a.sub())
print(a.mul())
print(a.div())

b= FourCal(3,7)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())


#2. 클래스의 상속
class FiveCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


c = FiveCal(9,5)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
print(c.pow())


#3. 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return print("0이 분모가 될 수 없습니다.")
        else:
            return self.first / self.second
        
d = SafeFourCal(10, 0)
print(d.add())
print(d.sub())
print(d.mul())
print(d.div())


#4. 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

        







    