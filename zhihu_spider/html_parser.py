from bs4 import BeautifulSoup
from urllib import parse
import re


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /topic/19551388
        links = soup.find_all('a', href=re.compile(r"/topic/\d"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <div class="topic-name zm-editable-status-normal" id="zh-topic-title"><h1 class="zm-editable-content" data-disabled="1">摄影</h1>
        title_node = soup.find('div', class_="topic-name").find("h1")
        res_data['topic'] = title_node.get_text()

        # <div class="zm-editable-content" data-editable-maxlength="130" data-disabled="1">
        content_node = soup.find('div', id="zh-topic-desc").find("div", class_="zm-editable-content")
        res_data['content'] = content_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
