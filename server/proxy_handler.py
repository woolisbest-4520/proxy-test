import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    # URLがhttpまたはhttpsで始まっていることを確認
    if not url.startswith(('http://', 'https://')):
        raise ValueError("URL must start with 'http://' or 'https://'")
    
    # リクエストを送信
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL: {url}")
    
    # レスポンスのHTMLを返す
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 必要に応じてJSやCSSの調整を行うことも可能
    # ここではそのままHTMLを返す
    return soup.prettify()
