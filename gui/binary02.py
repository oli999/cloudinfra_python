# gui/binary02.py

# 2진수 2개를 만들고 
a = 0b1100
b = 0b1010

# a 와 b 를 비트 AND 연산 (자리수 별로 모두가 1일때 결과가 1 이된다)
print(a & b)
print(bin(a&b))

# _ 는 visual separator (시각적으로만 구분하고 무시되는 기호)
info = 0b1111_1111_1111_0000

print(bin(info))

data1 = 0b1100_0011_1010_0001
data2 = 0b1100_0011_1010_0010
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100
data5 = 0b1111_0000_1010_1111

print(bin(info&data1))
print(bin(info&data2))
print(bin(info&data3))
print(bin(info&data4))
print(bin(info&data5))