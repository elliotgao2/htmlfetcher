from htmlfetcher import HTMLFetcher
fetcher = HTMLFetcher()
print(fetcher.get('https://www.baidu.com'))
fetcher.close()