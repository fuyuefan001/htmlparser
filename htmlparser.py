import requests
import urllib.request


def parse(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    with open('a.txt','w') as fp:
        fp.write(res.text)
    print(res.text)

def parse2(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    data=str(data, encoding = "utf-8")
    return (data)
    # with open('a.txt','w',encoding="utf-8") as fp:
    #     fp.write(data)


if __name__ == "__main__":
    url='https://www.amazon.com/Dell-Touchscreen-Quad-Core-MaxxAudio-Thunderbolt/dp/B07MDSLT8Z/ref=sr_1_2_sspa?crid=X9Y1D4UVT9H5&keywords=dell+xps+13+9370&qid=1554756304&s=gateway&sprefix=dell+xps+13%2Caps%2C162&sr=8-2-spons&psc=1'

    data=parse2(url)