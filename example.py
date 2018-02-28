from pprint import pprint

from htmlfetcher import HTMLFetcher
from htmlparsing import *

fetcher = HTMLFetcher()
text = fetcher.get('http://www.bpzufang.com/home', wait=5)
fetcher.close()
results = HTMLParsing(text).list('.stream-item', {'title': Text('.context-title'),
                                                  'user': Text('.author span'),
                                                  'time': Text('.time')})

pprint(results)
