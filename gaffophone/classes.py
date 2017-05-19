import praw
import datetime

class Gaffophone():
    def __init__(self):
        self.reddit = praw.Reddit('gaffophone')
        self.france =  self.reddit.subreddit("france")
        self.rance =  self.reddit.subreddit("rance")
        self.test = self.reddit.subreddit("testingground4bots")

    def run(self):
        text=[]
        title="Le meilleur de /r/rance, semaine {}".format(datetime.datetime.now().strftime("%V"))
        for submission in self.rance.top('week', limit=10):

            text.append(u'[{}]({}) par /u/{}\n'.format(submission.title, submission.url, submission.author).encode('utf-8'))
            print submission.title
            print submission.url


        self.test.submit(title, selftext="\n".join(text))

