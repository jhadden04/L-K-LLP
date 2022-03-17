import praw
import time
reddit = praw.Reddit(client_id='*******',
                     client_secret='*****',
                     user_agent='a reddit instance',
                     username='*****',
                     password='*****',  # I will change this
                     check_for_async=False)
trigger_phrases = ["why does this happen (1)", "why does that happen (2)"]  # phrases to trigger the bot, change and add to this to suit
comment_replies ["because of that (1)", "because of this (2)"]  # Phrases that respond to the trigger, 1 responds to 1 and 2 responds to 2
# Use lower case and keep the formatting the same as shown (" and , in the same places)
for comment in reddit.subreddit("finance+askreddit").stream.comments():  # change the subreddit names (finance+askreddit) for your desired subreddit: case-sensitive and needs the + sign between each new subreddit
 try:
  for i in range(len(trigger_phrases)):
    if trigger_phrases[i] in comment.body.lower():
      comment.reply(comment_replies[i])
 except:
   time.sleep(120)
