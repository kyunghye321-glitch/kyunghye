# 파이썬의 숫자는 "정수"와 소수 부분이 있는 "부동 소수점 수"를 제공한다.

# 1. 정수 (int)
a = 10
print(a)
print(type(a))

# 2. 실수 (float): 오차를 가진다
b = 3.14
print(b)
print(type(b))

# 3. 복소수 (complex)
c = 3 + 4j
print(c)
print(type(c))

# 4. 논리값 (bool)
d = True
print(d)
print(type(d))

# 5. 문자열 (str)
e = "Python"
print(e)
print(type(e))

# 6. 리스트 (list)
f = [1, 2, 3]
print(f)
print(type(f))

# 7. 튜플 (tuple)
g = (1, 2, 3)
print(g)
print(type(g))

# 8. 딕셔너리 (dict)
h = {"a": 1}
print(h)
print(type(h))

# 9. 집합 (set)
i = {1, 2, 3}
print(i)
print(type(i))

# 10. 범위 (range)
j = range(5)
print(j)
print(type(j))

# 11. 바이트 (bytes)
k = b"abc"
print(k)
print(type(k))

# 12. 바이트배열 (bytearray)
l = bytearray(b"abc")
print(l)
print(type(l))

# 13. 없음 (NoneType)
m = None
print(m)
print(type(m))

# 14. 함수 (function)
def hello():
    print("Hello")

print(hello)
print(type(hello))

# 15. 모듈 (module)
import math

print(math)
print(type(math))

# 16. 클래스 (type)
class Person:
    pass

print(Person)
print(type(Person))

print("commit push test")

#== : 객체의 값만 비교 || is : 객체 비교

#>> Error: = 는 연산자(operator)가 아니라 대입문(statement)이기 때문
# n = 10
# result = (x = n>5)   # 대입하면서 값
# print(result)
#= : 대입문 → 값을 반환하지 않음 || := : 대입 연산자 → 값을 반환함

# := 월러스 연산자 사용, result = 우측 표현식 자리에 대입문이 아닌 대입연산자(:=)를 사용 
# 월러스 연산자는 왼쪽변수에 우측 값을 할당하고 할당된 값을 반환하는 대입연산자

n = 10
result = (x := n>5)   # 대입하면서 값 반환
print(result)