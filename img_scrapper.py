import requests

def img_scraper(url):
    response=requests.get(url, stream=True)
    if response.status_code == 200:
        img=response.content
        with open("hasil.png", "wb") as f:
            f.write(img)