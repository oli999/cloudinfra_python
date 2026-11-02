# Step07_Operator.py

'''
    여러가지 연산자 사용해 보기
'''

# 1. 논리 연산자 : bool type 데이터를 연산 ( and, or, not)

print("-- or 연산 --")
print("False or False :", False or False)  # False
print("False or True :", False or True)    # True
print("True or False :", True or False)    # True
print("True or True :", True or True)      # True

print("-- and 연산 --")
print("False and False :", False and False) # False
print("False and True :", False and True)   # False
print("True and False :", True and False)   # False
print("True and True :", True and True)     # True

print("-- not 연산 --")
print("not True :", not True)   # False
print("not False :", not False) # True

# 2. 대입연산자 : =, +=, -=, *=, /=, %=

name = "kimgura"
num = 10

# num = num + 1
num += 1 
# num = num + 5
num += 5
# num = num - 1
num -= 1
# num = num - 3
num -= 3
# num = num * 2
num *= 2
# num = num / 3
# Python 3에서 / 연산은 항상 실수(float) 결과를 반환합니다.
num /= 3
# % 는 나머지 연산자 ( num 을 3으로 나눈 나머지값을 얻어낸다 )
# num = num % 3
num %= 3

# 3. 비교 연산자 : == , != , >, >= , <, <=
# 비교 연산의 결과는 bool type 으로 나타난다.

print("10 == 10 : ", 10 == 10)
print("10 != 10 : ", 10 != 10)
print("10 > 20 : ", 10 > 20)
print("10 >= 20 :", 10 >= 20)
result = 10 < 20
print("result : ", result)

is_equal = "abcd" == "abcd"
is_different = "1234" != "1234"
print("is_equal : ", is_equal)
print("is_different : ", is_different)

# 4. 산술 연산자 : +, -, *, /, //, %, **
# 숫자형(int, float) 데이터의 수학적 계산을 수행합니다.

print("-- 산술 연산 --")
print("10 + 3 :", 10 + 3)   # 13 (더하기)
print("10 - 3 :", 10 - 3)   # 7 (빼기)
print("10 * 3 :", 10 * 3)   # 30 (곱하기)

# / 연산은 항상 실수(float) 결과를 반환합니다.
print("10 / 3 :", 10 / 3)   # 3.3333333333333335 (나누기)

# // 연산은 나누기 결과에서 소수점 이하를 버리고 정수(몫)만 반환합니다.
print("10 // 3 :", 10 // 3) # 3 (몫)

# % 연산은 나눈 후 남은 나머지 값을 반환하며, 짝수/홀수 판별이나 배수 판별에 자주 쓰입니다.
print("10 % 3 :", 10 % 3)   # 1 (나머지)

# ** 연산은 거듭제곱을 수행합니다.
print("10 ** 3 :", 10 ** 3) # 1000 (거듭제곱, 10의 3승)