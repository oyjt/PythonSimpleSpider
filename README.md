# PythonSimpleSpider
用Python写的简单的爬虫，包含百度百科的爬虫和知乎爬虫

## 环境
Python 3.5+

## 依赖
```python
pip install beautifulsoup4
```

## 结构
| 文件        | 模块   |  描述  |
| :----:   | :----:  | :----:  |
|spider_main | 程序控制模块 | 程序入口和控制中心 |
|url_manager | 链接管理模块 | 管理链接集合与信息 |
|html_downloader | 网页下载模块 | 根据URL获取HTML源码 |
|html_parser | 网页解析模块 | 根据HTML源码获取数据 |
|html_outputer | 数据输出模块 | 将数据以MD格式存储 |

## 启动
python spider_main.py

