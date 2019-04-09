# import requests
import urllib.request
import html.parser
from html.parser import HTMLParser
from bs4 import BeautifulSoup
comment=[]
dataslice=[]
def url2html(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    data=str(data, encoding = "utf-8")
    return (data)

def crawl(string):
    soup1 = BeautifulSoup(string,'html')
    result1 = soup1.find_all(attrs={"class":"a-expander-content reviewText review-text-content a-expander-partial-collapse-content"})
    hp_ins=hp()
    # hp_ins.feed(data=html)
    # hp_ins.dataslice=[]
    for res in result1:
        print(res)
        hp_ins.dataslice = []
        hp_ins.feed(data=str(res))
        comment.append(hp_ins.dataslice)
class hp(HTMLParser):
    flg=0
    dataslice=[]
    def handle_starttag(self, tag, attr):
        if tag=='span':#目标标签
            for a in attr:
                # print(a)
                if a[0]=='class' and a[1]=='':
                    self.flg=1
                    break
        else:
            pass

    def handle_endtag(self,tag):
        if tag == 'span':
            self.flg=0

    def handle_data(self, data):
        if self.flg==1:
            # print(data)
            self.dataslice.append(data)



if __name__ == "__main__":
    url='https://www.amazon.com/Intel-i7-8700-Desktop-Processor-Cores/product-reviews/B07598HLB4/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    html=url2html(url)

    fp= open('html.txt','r')
    html=fp.read()
    # print(html)
    # with open('html.txt','w',encoding="utf-8") as fp:
    #     fp.write(html)

    crawl(str(html))
    with open('comments.txt','w') as fp:

        for c in comment:
            fp.write(str(c))
            fp.write('\n')
