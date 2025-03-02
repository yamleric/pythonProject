import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
count = 1
for start_num in range(0,250,25):
    print(start_num)
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    # for title in all_titles:
    #     title_string = title.string
    #     if "/" not in title_string:
    #         print(title_string)

#

#     all_titles = soup.findAll("span",attrs={"class":"title"})
#     for title in all_titles:
#         title_string = title.string
#         if "/" not in title_string:
#             print(title.string)
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
# }
#
# # 初始化一个计数器来记录序号
# count = 1
#
# for start_num in range(0, 250, 25):
#     response = requests.get(f"https://movie.douban.com/top250?={start_num}", headers=headers)
#     html = response.text
#     soup = BeautifulSoup(html, "html.parser")
#     all_titles = soup.findAll("span", attrs={"class": "title"})
    with open('douban_top250_titles.txt', 'a', encoding='utf-8') as f:
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:
                f.write(f"{count}. {title_string}\n")
                count += 1


# ... 其他代码


