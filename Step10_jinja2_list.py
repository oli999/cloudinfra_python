# Step10_jinja2_list.py

from jinja2 import Template


sample = '''
    {% for item in [10,20,30] %}
    - {{ item }}
    {% endfor %}
'''

t1:Template = Template(sample)
result1 = t1.render()
print(result1)

print("---")

# 좌측(테그 앞쪽)의 공백 개행제거  =>  {%- 
sample2 = '''
    {%- for item in [10,20,30] %}
    - {{ item }}
    {%- endfor %}
'''

t2:Template = Template(sample2)
result2 = t2.render()
print(result2)

print("---")

# 외부에서 nums 에 list 를 전달해야 정상동작하는 템플릿 
sample3 = '''
    {%- for item in nums %}
    - {{ item }}
    {%- endfor %}
'''
t3:Template = Template(sample3)
# Template 객체에 전달할 데이터가 준비 되어 있다고 가정
data = [10, 20, 30]
# render() 함수 호출하면서 nums 라는 매개변수에 data 전달하기 
result3:str = t3.render(nums=data)
# 결과 확인 
print(result3)

