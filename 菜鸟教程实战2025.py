# from bs4 import BeautifulSoup
#
# # HTML 文本
# html_text = """
# [<div class="design" id="leftcolumn">
# <a data-p="par" href="/python3/python3-tutorial.html" target="_top" title="Python3 教程">
# 			Python3 教程			</a>
# <a href="python3-intro.html" target="_top" title="Python3 简介"> Python3 简介 </a>
# <a href="python3-install.html" target="_top" title="Python3 环境搭建"> Python3 环境搭建</a>
# <a href="python-vscode-setup.html" target="_top" title="Python3 VScode"> Python3 VScode </a>
# <a href="/python3/fitten-code.html" target="_top" title="Python3 AI 编程助手">Python3 AI 编程助手</a>
# <a href="python3-basic-syntax.html" target="_top" title="Python3 基础语法"> Python3 基础语法 </a>
# <a href="python3-data-type.html" target="_top" title="Python3 基本数据类型"> Python3 基本数据类型 </a>
# <a href="python3-type-conversion.html" target="_top" title="Python3  数据类型转换"> Python3 数据类型转换 </a>
# <a data-p="par" href="/python3/python3-interpreter.html" target="_top" title="Python3 解释器">
# 			Python3 解释器			</a>
# <a data-p="par" href="/python3/python3-comment.html" target="_top" title="Python3 注释">
# 			Python3 注释			</a>
# <a href="python3-basic-operators.html" target="_top" title="Python3 运算符"> Python3 运算符 </a> <a data-p="par" href="/python3/python3-number.html" target="_top" title="Python3 数字(Number)">
# 			Python3 数字(Number)			</a>
# <a data-p="par" href="/python3/python3-string.html" target="_top" title="Python3 字符串">
# 			Python3 字符串			</a>
# <a data-p="par" href="/python3/python3-list.html" target="_top" title="Python3 列表">
# 			Python3 列表			</a>
# <a href="python3-tuple.html" target="_top" title="Python3 元组"> Python3 元组 </a>
# <a href="python3-dictionary.html" target="_top" title="Python3 字典"> Python3 字典</a>
# <a href="python3-set.html" target="_top" title="Python3 集合"> Python3 集合</a> <a data-p="par" href="/python3/python3-conditional-statements.html" target="_top" title="Python3 条件控制">
# 			Python3 条件控制			</a>
# <a data-p="par" href="/python3/python3-loop.html" target="_top" title="Python3 循环语句">
# 			Python3 循环语句			</a>
# <a href="python3-step1.html" target="_top" title="Python3 编程第一步"> Python3 编程第一步</a>
# <a href="python-comprehensions.html" target="_top" title="Python3 推导式"> Python3 推导式 </a>
# <a href="python3-iterator-generator.html" target="_top" title="Python3 迭代器与生成器"> Python3 迭代器与生成器</a> <a data-p="par" href="/python3/python3-function.html" target="_top" title="Python3 函数">
# 			Python3 函数			</a>
# <a href="python-lambda.html" target="_top" title="Python3 lambda（匿名函数）"> Python3 lambda </a>
# <a href="python-decorators.html" target="_top" title="Python 装饰器"> Python3 装饰器 </a> <a data-p="par" href="/python3/python3-data-structure.html" target="_top" title="Python3 数据结构">
# 			Python3 数据结构			</a>
# <a data-p="par" href="/python3/python3-module.html" target="_top" title="Python3 模块">
# 			Python3 模块			</a>
# <a data-p="par" href="/python3/python3-inputoutput.html" target="_top" title="Python3 输入和输出">
# 			Python3 输入和输出			</a>
# <a href="python3-file-methods.html" target="_top" title="Python3 File"> Python3 File </a>
# <a href="python3-os-file-methods.html" target="_top" title="Python3 OS"> Python3 OS </a> <a data-p="par" href="/python3/python3-errors-execptions.html" target="_top" title="Python3 错误和异常">
# 			Python3 错误和异常			</a>
# <a data-p="par" href="/python3/python3-class.html" target="_top" title="Python3 面向对象">
# 			Python3 面向对象			</a>
# <a href="/python3/python3-namespace-scope.html" target="_top" title=" Python3 命名空间/作用域"> Python3 命名空间/作用域</a> <a data-p="par" href="/python3/python3-stdlib.html" target="_top" title="Python3 标准库概览">
# 			Python3 标准库概览			</a>
# <a data-p="par" href="/python3/python3-examples.html" target="_top" title="Python3 实例">
# 			Python3 实例			</a>
# <a href="/quiz/python-quiz.html" target="_blank" title="Python 测验"> Python 测验 </a>
# <br/><h2 class="left"><span class="left_h2">Python3</span> 高级教程</h2> <a data-p="par" href="/python3/python3-reg-expressions.html" target="_top" title="Python3 正则表达式">
# 			Python3 正则表达式			</a>
# <a data-p="par" href="/python3/python3-cgi-programming.html" target="_top" title="Python3 CGI编程">
# 			Python3 CGI编程			</a>
# <a href="python-mysql-connector.html" target="_top" title="Python MySQL - mysql-connector 驱动">Python3 MySQL(mysql-connector)</a> <a data-p="par" href="/python3/python3-mysql.html" target="_top" title="Python3 MySQL 数据库连接 – PyMySQL 驱动">
# 			Python3 MySQL(PyMySQL)			</a>
# <a data-p="par" href="/python3/python3-socket.html" target="_top" title="Python3 网络编程">
# 			Python3 网络编程			</a>
# <a data-p="par" href="/python3/python3-smtp.html" target="_top" title="Python3 SMTP发送邮件">
# 			Python3 SMTP发送邮件			</a>
# <a data-p="par" href="/python3/python3-multithreading.html" target="_top" title="Python3 多线程">
# 			Python3 多线程			</a>
# <a data-p="par" href="/python3/python3-xml-processing.html" target="_top" title="Python3 XML 解析">
# 			Python3 XML 解析			</a>
# <a data-p="par" href="/python3/python3-json.html" target="_top" title="Python3 JSON 数据解析">
# 			Python3 JSON			</a>
# <a data-p="par" href="/python3/python3-date-time.html" target="_top" title="Python3 日期和时间">
# 			Python3 日期和时间			</a>
# <a data-p="par" href="/python3/python3-built-in-functions.html" target="_top" title="Python3 内置函数">
# 			Python3 内置函数			</a>
# <a data-p="par" href="/python3/python-mongodb.html" target="_top" title="Python MongoDB">
# 			Python3 MongoDB			</a>
# <a href="python-urllib.html" target="_top" title="Python3 urllib"> Python3 urllib</a> <a data-p="par" href="/python3/python-uwsgi.html" target="_top" title="Python uWSGI  安装配置">
# 			Python uWSGI  安装配置			</a>
# <a data-p="par" href="/python3/python3-pip.html" target="_top" title="Python3 pip">
# 			Python3 pip			</a>
# <a data-p="par" href="/python3/python-operator.html" target="_top" title="Python3 operator 模块">
# 			Python3 operator			</a>
# <a data-p="par" href="/python3/python-math.html" target="_top" title="Python math 模块">
# 			Python math			</a>
# <a data-p="par" href="/python3/python-requests.html" target="_top" title="Python requests 模块">
# 			Python requests			</a>
# <a data-p="par" href="/python3/python-random.html" target="_top" title="Python random 模块">
# 			Python random			</a>
# <a data-p="par" href="/python3/python3-resources.html" target="_top" title="Python 有用的资源">
# 			Python 有用的资源			</a>
# <a data-p="par" href="/python3/python-ai-draw.html" target="_top" title="Python AI 绘画">
# 			Python AI 绘画			</a>
# <a data-p="par" href="/python3/python-statistics.html" target="_top" title="Python statistics 模块">
# 			Python statistics			</a>
# <a data-p="par" href="/python3/python-hashlib.html" target="_top" title="Python hashlib 模块">
# 			Python hashlib			</a>
# <a data-p="par" href="/python3/python-qt.html" target="_top" title="Python 量化">
# 			Python 量化			</a>
# <a data-p="par" href="/python3/python-pyecharts.html" target="_top" title="Python pyecharts 模块">
# 			Python pyecharts			</a>
# </div>]
# """
#
# # 创建 BeautifulSoup 对象
# soup = BeautifulSoup(html_text, 'html.parser')
#
# # 找到所有的 <a> 标签
# all_links = soup.find_all('a')
#
# # 提取每个 <a> 标签的 title 属性值
# for link in all_links:
#     title = link.get('title')
#     print(title)
import requests
from bs4 import BeautifulSoup
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.runoob.com/',
}


def sanitize_filename(title):
    """清理文件名中的非法字符"""
    return re.sub(r'[\\/*?:"<>|]', '_', title).strip()


def main():
    # 获取目录页
    url = 'https://www.runoob.com/python3/python3-tutorial.html'
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求目录页失败: {e}")
        return

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 关键修复1：通过 id="leftcolumn" 定位导航栏
    nav_list = soup.find('div', id='leftcolumn')
    if not nav_list:
        print("未找到教程链接区域")
        return

    # 提取教程链接（精确过滤）
    tutorial_urls = []
    for link in nav_list.find_all('a', href=True):
        href = link['href']
        if href.startswith('/python3/') and href.endswith('.html'):
            full_url = 'https://www.runoob.com' + href
            if full_url not in tutorial_urls:  # 去重
                tutorial_urls.append(full_url)

    print(f"已提取到 {len(tutorial_urls)} 个教程链接")

    # 爬取每个教程
    for url in tutorial_urls:
        try:
            time.sleep(1.5)  # 降低请求频率
            print(f"正在爬取: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            # 修正标题提取逻辑
            article_intro = soup.find('div', class_='article-intro') or soup.find(id='content')
            title = "未命名教程"
            if article_intro:
                title_tag = article_intro.find('h1')
                title = title_tag.text.strip() if title_tag else title

            # 提取正文内容
            content_div = soup.find('div', class_='article-body')
            content = content_div.text.strip() if content_div else "未找到正文"

            # 保存文件
            safe_title = sanitize_filename(title)
            filename = f"{safe_title}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"已保存: {filename}")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {url} - {e}")
        except Exception as e:
            print(f"处理 {url} 时出错: {e}")


if __name__ == "__main__":
    main()