import praw
import time
reddit = praw.Reddit(client_id='aCsxA497160GjRop_8DDXA',
                     client_secret='rAuMc2mxJPwLMsX4xYqNrpg5ifa7ig',
                     user_agent='a reddit instance',
                     username='DistinctCap2574',
                     password='this is the password',
                     check_for_async=False)
trigger_phrases = ["why does this happen (1)", "why does that happen (2)"]
comment_replies ["because of that (1)", "because of this (2)"]
:
for comment in reddit.subreddit("finance+askreddit").stream.comments():
 try:
  for i in range(len(trigger_phrases)):
    if trigger_phrases[i] in comment.body.lower():
      comment.reply(comment_replies[i])
 except:
   time.sleep(120)
