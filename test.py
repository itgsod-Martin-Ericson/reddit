from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
import pprint
from reddit.post import Post
from reddit.save import Save

bojohan = client.login('doktoret')

#bojohan.me()

pics = Subreddit("pics")
#print pics.hot_children()[0]['data']['url']
#print pics.hot_children()[0]['data']['name']

data = pics.hot_children()[0]

for dick in pics.hot_children():
    tities = Post("pics", dick)
    nig = tities.image()
    weed = Save(nig).save_image()

post = Post("pics", data)
print post.image()

save = Save(post.image()).save_image()

# python = Subreddit("python")
#
# python.hot()








