import reddit

class Post(object):
    def __init__(self, subreddit, post_data):
        self.post_data = post_data
        self.subreddit = subreddit

    def data(self):
        return self.post_data['data']

    def image(self):
        if self.data()['domain'] == "i.imgur.com":
            return self.data()['url']
        else:
            return "This is not an imgur image."
