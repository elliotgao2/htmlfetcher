from htmlfetcher import HTMLFetcher

fetcher = HTMLFetcher(browser='/home/bug/桌面/geckodriver')
text = fetcher.get('http://zhaopin.baidu.com/quanzhi?tid=4139&ie=utf8&oe=utf8&query=python&city_sug=%E6%88%90%E9%83%BD')
fetcher.close()

print(text)
