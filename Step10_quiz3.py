# Step10_quiz3.py

# Template 클래스 import
from jinja2 import Template

# DB 에서 읽어온 글 목록이라고 가정하자 
posts:list = [
    {"id":1, "writer":"작성자1", "title":"제목1"},
    {"id":2, "writer":"작성자2", "title":"제목2"},
    {"id":3, "writer":"작성자3", "title":"제목3"}
]

'''
    위의 posts 에 담긴 데이터를 이용해서 아래와 같이 출력되도록 해 보세요  

글목록 입니다
- 글번호: 1  작성자: 작성자1  제목: 제목1
- 글번호: 2  작성자: 작성자2  제목: 제목2
- 글번호: 3  작성자: 작성자3  제목: 제목3
'''

sample = '''
글목록 입니다
{%- for item in posts %}
- 글번호: {{item.id}} 작성자: {{item.writer}} 제목: {{item.title}} 
{%- endfor %}
'''

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>글목록</title>
</head>
<body>
    <h1>글목록입니다</h1>
    <table>
        <tr>
            <th>번호</th>
            <th>작성자</th>
            <th>제목</th>
        </tr>
        {%- for item in posts %}
        <tr>
            <td>{{ item.id }}</td>
            <td>{{ item.writer }}</td>
            <td>{{ item.title }}</td>
        </tr>
        {%- endfor %}
    </table>
</body>
</html>
'''

# Template 클래스를 이용해서 템플릿 객체를 생성
t1:Template = Template(html)

# posts 라는 키값으로 posts 변수 안에 들어 있는 값을 전달
result = t1.render(posts=posts)

print(result)