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
    result1 = soup1.find_all(attrs={"id":"data"})
    hp_ins=hp()
    # hp_ins.feed(data=html)
    # hp_ins.dataslice=[]
    print(len(result1))
    for res in result1:
        print(res)
        # hp_ins.dataslice = []
        # hp_ins.feed(data=str(res))
        # comment.append(hp_ins.dataslice)
class hp(HTMLParser):
    flg=0
    dataslice=[]
    def handle_starttag(self, tag, attr):
        if tag=='script':#目标标签
            for a in attr:
                # print(a)
                if a[0]=='if' and a[1]=='data':
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
    # url='https://www.amazon.com/EVGA-GeForce-GAMING-Graphics-08G-P4-2183-KR/dp/B07GHVK4KN?pd_rd_w=Nhuyw&pf_rd_p=0fc3f2c4-3ed5-4d11-9995-8d7c82394713&pf_rd_r=6MJGR2DZYYC2AZG5M77N&pd_rd_r=f37e4484-7351-41ce-8e16-e1096503464c&pd_rd_wg=QAPTY&ref_=pd_gw_cr_simh'
    # url='https://www.reddit.com/r/explainlikeimfive/comments/1p91ha/eli5_why_is_fluoride_in_water_so_bad/?sort=top'
    # html=url2html(url)

    fp= open('html.txt','r',encoding='utf-8')
    html=fp.read()
    # print(html)
    with open('html.txt','w',encoding="utf-8") as fp:
        fp.write(html)

    crawl(str(html))
    with open('comments.txt','w') as fp:

        for c in comment:
            fp.write(str(c))
            fp.write('\n')
