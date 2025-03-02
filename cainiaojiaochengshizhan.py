
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

response = requests.get("https://www.runoob.com/python3/", headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# 获取所有 class 为 "design" 的 div 元素中的所有 a 标签
all_a_tags = soup.find_all("a", class_="design")  # 可以简写成 class_="design"

# 循环遍历并打印每个 a 标签的 title 属性
for a_tag in all_a_tags:
    title = a_tag.get('title')
    if title:  # 可选，判断 title 是否存在才打印
        print(title)




status_code = response.status_code
print(status_code)
