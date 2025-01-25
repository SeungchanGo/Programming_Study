#딕셔너리 자료형

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1188'}
a = {1: 'hi'}
b = {'a':[1,2,3]}


#딕셔너리 쌍 추가 & 삭제
a = {1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)


#딕셔너리를 사용하는 방법 ~ 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'juliet': 90}
print(grade['pey'])
print(grade['juliet'])


#딕셔너리 관련 함수
#1. Key 리스트 만들기 (keys)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1188'}
print(a.keys())

for k in a.keys():
    print(k)

#1-1. keys 객체를 리스트로 반환 
print(list(a.keys()))

#2. Value 리스트 만들기 (values)
print(a.values())

#3. Key, Value 쌍 얻기 (items)
print(a.items())

#4. Key:Value 쌍 모두 지우기 (clear)
print(a.clear())

#5. Key로 Value 얻기 (get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1188'}
print(a.get('name'))
print(a.get('phone'))

#6. 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
print('name' in a)
print('email' in a)
