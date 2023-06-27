import requests
from bs4 import BeautifulSoup
import json
import random
from urllib.parse import urlparse, parse_qs

# 定义 User-Agent 列表，随机选择一个 User-Agent
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
]

# 随机选择一个 User-Agent
user_agent = random.choice(user_agent_list)

# 设置请求头中的 User-Agent 字段
headers = {
    'User-Agent': user_agent
}

url = 'https://movie.douban.com/j/search_subjects'

params = {
    'type': 'movie',
    'tag': '豆瓣高分',
    'page_start': '0',
    'page_limit': '1'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    for movie in data['subjects']:
        movie_url = movie['url']
        response = requests.get(movie_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 提取导演名称
            director = soup.find('a', rel='v:directedBy')
            if director is not None:
                movie['director'] = director.text
            else:
                movie['director'] = '未知'

            # 提取主演
            actors = []
            for i, actor in enumerate(soup.find_all('a', rel='v:starring')):
                if i == 4:
                    break
                actors.append(actor.text)
            if len(actors) > 0:
                movie['actor'] = '/'.join(actors)
            else:
                movie['actor'] = '未知'

            # 提取制片国家/地区
            region = soup.find('span', class_='pl', string='制片国家/地区:')
            if region is not None:
                movie['area'] = region.next_sibling.strip()
            else:
                movie['area'] = '未知'

            # 提取剧情简介
            plot_summary = soup.find('span', property='v:summary')
            if plot_summary is not None:
                movie['desc'] = plot_summary.text.strip().replace('\n', '')
            else:
                movie['desc'] = '暂无简介'

            # 提取上映年份
            release_date = soup.find('span', property='v:initialReleaseDate')
            if release_date is not None:
                movie['years'] = release_date.text[:4]
            else:
                movie['years'] = '未知'

            # 提取播放源
            sources = []
            for a in soup.find_all('a', class_='playBtn'):
                name = a['data-cn']
                url = parse_qs(urlparse(a['href']).query)['url'][0]
                sources.append({'Name': name, 'Url': url})
            if len(sources) > 0:
                movie['sources'] = sources
            else:
                movie['sources'] = []
        else:
            movie['desc'] = '暂无简介'
            movie['area'] = '未知'
            movie['actor'] = '未知'
            movie['director'] = '未知'
            movie['years'] = '未知'
            movie['sources'] = []

        # 一些特殊字段处理
        movie['imgUrl'] = movie['cover']
        movie['cateName'] = '电影'
        movie['catId'] = 0
    with open('douban_top50_movies.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('数据已保存到 douban_top50_movies.json 文件中')
else:
    print('请求异常，状态码为', response.status_code)