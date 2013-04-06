#coding:utf-8
import webapp2
import tweepy
import os
from google.appengine.ext.webapp import template


CONSUMER_KEY="********************"
CONSUMER_SECRET="********************"
ACCESS_KEY="********************"
ACCESS_SECRET="********************"

def twitterListMembers(username,listName):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    result=[]
    result_1=[]
    for i in tweepy.Cursor(api.list_members,username,listName).items():
        result.append([i.profile_image_url,i.screen_name,i.name,i.followers_count,i.friends_count,i.statuses_count])
    for i in  sorted(result, key=lambda x:x[3], reverse=True):
        result_1.append([i[0],i[1],i[2],i[3],i[4],i[5]])
    return result_1

class MainPage(webapp2.RequestHandler):


    def get(self):
        params = {'username':"　　　",'listname':"　　　　　",'datas':[["","","","","",""]]}
        fpath = os.path.join(os.path.dirname(__file__),'index.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)
    def post(self):
        a=self.request.get("username").split("/")
        username,listname = a[0],a[1]
        params = {'username':username,'listname':listname,'datas':twitterListMembers(username,listname)}
        fpath = os.path.join(os.path.dirname(__file__),'index.html')
        html = template.render(fpath,params)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)




app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)