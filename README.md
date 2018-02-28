# HTML Parsing

No pain HTML fetching library. A light wrapper of selenium
For page with a lot of ajax.


## Installation

```python
pip install htmlfetcher
```

## Usage

```python
from htmlfetcher import HTMLFetcher
fetcher = HTMLFetcher()
fetcher.get('https://www.baidu.com')
fetcher.close()
```
