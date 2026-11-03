# Step10_quiz.py

from jinja2 import Template


data = ["김구라", "해골", "원숭이"]

'''
    data (list) 에 들어있는 정보를 이용해서 아래와 동일한 형식의 문자열을 얻어내는 프로그래밍을 해 보세요.

<ul>
    <li>김구라</li>
    <li>해골</li>
    <li>원숭이</li>
</ul>

    결과를 콘솔창에 출력해 보세요. 
'''

sample = '''
<ul>
    {%- for item in names %}
    <li>{{ item }}</li>
    {%- endfor %}
</ul>
'''

t1:Template = Template(sample)
result1:str = t1.render(names=data)
print(result1)

data2 = ["주뎅이","덩어리","개다리"]
result2:str = t1.render(names=data2)
print(result2)



