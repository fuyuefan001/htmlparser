import praw
import pandas as pd
import datetime as dt
def printsub(level,tab,file):
    if file==None:
        print(tab+level.body)
        for x in level._replies._comments:
            tab+='____ '
            try :
                printsub(x,tab)
            except Exception as e:
                pass
                print('')
    else:
        file.write(tab+level.body+'\n')
        for x in level._replies._comments:
            tab+='____ '
            try :
                # file.write('\n')
                printsub(x,tab,file)
            except Exception as e:
                pass
                # file.write('\n')
if __name__=='__main__':
    reddit = praw.Reddit(user_agent='get comments from reddit',
                         client_id='ZVfl78laZwzW8g', client_secret="eIqFLTDTM4UAP2PZerdvyT7Meec",
                         username='fuyuefan001', password='Q1q2q3q4')
    sub = reddit.submission(url='https://www.reddit.com/r/explainlikeimfive/comments/1p91ha/eli5_why_is_fluoride_in_water_so_bad/?sort=top')
    # submission = reddit.submission(id='3g1jfi')
    fp=open('redditcomment.txt','w')
    for top_level_comment in sub.comments:
        printsub(top_level_comment,'',file=fp)

