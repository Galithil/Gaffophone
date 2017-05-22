import praw
import datetime
import codecs


class Gaffophone():
    def __init__(self, args):
        self.reddit = praw.Reddit('gaffophone')
        self.france =  self.reddit.subreddit("france")
        self.rance =  self.reddit.subreddit("rance")
        self.test = self.reddit.subreddit("testingground4bots")
        self.body_template = args.body_template
        self.title_template = args.title_template
        self.submission_template = args.submission_template

    def run(self):
        submissions=[]
        with codecs.open(self.title_template, 'r', 'utf-8') as tt:
            title = tt.read().encode('utf-8').format(weeknumber=datetime.datetime.now().strftime("%V"))

        with codecs.open(self.body_template, 'r', 'utf-8') as bt:
            body = bt.read().encode('utf-8')

        with codecs.open(self.submission_template, 'r', 'utf-8') as st:
            sub_temp = st.read().encode('utf-8')
        for submission in self.rance.top('week', limit=10):
            submissions.append(sub_temp.format(submission_title=submission.title.encode('utf-8'), 
                                               submission_url=submission.url.encode('utf-8'), user=submission.author,
                                               comments_url=submission.permalink.encode('utf-8')))

        post = body.format(submissions="\n".join(submissions))

        self.test.submit(title, selftext=post)

