"""
spider.py用于采集新闻信息
"""

import requests
from bs4 import BeautifulSoup
SESSION = requests.session()

URL = "http://nsearch.chosun.com/search/total.search?query=%EC%A4%91%EA%B5%AD&siteid=&category=&sort=1&writer=&field=paper&date_period=&date_start=20120101&date_end=20191125&emd_word=&expt_word=&opt_chk="
HEADERS = {
	"Host": "nsearch.chosun.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
NEWS_HEADERS = {
	"Host": "news.chosun.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}


def request_html(url, headers):
	"""获取html源码"""
	response = SESSION.get(url=url, headers=headers)
	html = response.content.decode(encoding='utf-8')
	return html


def get_url(html):
	"""获取下一页的url链接和当页的所有新闻链接"""
	soup = BeautifulSoup(html, "html.parser")
	dl_list = soup.find_all("dl", {"class": "search_news"})
	url_list = []
	for dl in dl_list:
		href = dl.find("a").get("href")
		url_list.append(href)
	a = soup.find("a", {"class": "next"})
	next_url = a.get("href")
	if not next_url: return None, None
	next_url = "http://nsearch.chosun.com/search/" + next_url
	print(f"next_url:{next_url}")
	return next_url, url_list


def request_news(url):
	html = request_html(url=url, headers=NEWS_HEADERS)
	print(f"request_news=>html:{html}")


def save(title, context, path="./"):
	with open(f"{path}{title}.txt", mode="w", encoding="utf-8") as out:
		out.write(context)


def main():
	html = request_html(url=URL, headers=HEADERS)
	next_url, url_list = get_url(html)
	while next_url is not None:
		# 根据url_list捕获存储新闻信息
		for url in url_list:
			print(f"url:{url}")
			request_news(url=url)
			break
		break
		# 获取下一个url和当前页的新闻url_list
		# html = request_html(url=next_url)
		# next_url, url_list = get_url(html)


if __name__ == '__main__':
	main()
# save(title=title, context=context)
