
# list type 에 대해서 알아보기

nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", "choi"]

# list 에 들어 있는 데이터를 앞에서 부터 순서대로 참조하면서 어떤 동작을 할일이 많다.

# nums 에 저장되어 있는 데이터를 순서대로 참조하면서 콘솔창에 출력하기

for item in nums:
    print(item)

# names 에 들어 있는 데이터를 순서대로 참조하면서 콘솔창에 출력하는 코드를 작성해 보세요.
for item in names:
    print(item)

# range() 함수의 동작을 확인해 보자 
r1 = range(5)
r2 = range(10)

print(r1)
print(r2)

for item in range(5):
    print(item)

# list에 저장된 item 을 index 를 이용해서 참조 하고 싶다면
for i in range(len(names)):
    print("list 의 index 와 함께 출력합니다")
    print(i, names[i])