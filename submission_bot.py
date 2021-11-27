import praw
import time

from praw.reddit import Subreddit


reddit = praw.Reddit("bot1", user_agent='cs40bot')

Subreddit = reddit.subreddit("Kitten").top(limit=50)
for post in Subreddit:
    print('title=', post.title)
    reddit.subreddit("BotTownFriends").submit(title=post.title, url=post.url )
