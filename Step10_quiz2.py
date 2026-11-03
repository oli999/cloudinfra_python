# Step10_quiz2.py
'''
    info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열을 출력해 보세요.
---
번호: 1
이름: 김구라
키: 180 cm
몸무게: 80 kg
취미 : 
    - 피아노  
    - 당구  
    - 프로그래밍
---

'''


from jinja2 import Template

# 템플릿에 렌더링할 데이터 딕셔너리 정의
info:dict = {
    "num": 1,
    "name": "김구라",
    "body": {
        "height": 180,
        "weight": 80
    },
    "hobby": ["피아노", "당구", "프로그래밍"]
}

# 딕셔너리의 키(key) 이름을 템플릿 변수로 직접 사용하는 구조
sample = '''
---
번호: {{ num }}
이름: {{ name }}
키: {{ body.height }} cm
몸무게: {{ body.weight }} kg
취미 : 
{%- for item in hobby %}
    - {{ item }}
{%- endfor %}
---
'''

# 템플릿 객체 생성
t = Template(sample)

# 딕셔너리 객체를 직접 전달하여 내부 키들을 템플릿 컨텍스트 변수로 언패킹(Unpacking)
result = t.render(info)

# 결과물 앞뒤의 불필요한 공백과 개행 기호를 제거한 후 출력
print(result.strip())