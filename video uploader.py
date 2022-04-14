import scrapetube
import praw
import time
from pytube import YouTube

reddit = praw.Reddit(client_id='*******',
                     client_secret='*****',
                     user_agent='a reddit instance',
                     username='*****',
                     password='*****',
                     check_for_async=False)  # once again, these need to be filled in, but it isn't safe to fill them in when the file is public


def links():
    videos = scrapetube.get_channel("UCTFOmHms9SZCsHiwvvRmsig") # Y&K YT channel id
    start = 'https://www.youtube.com/watch?v='
    urls = []
    for video in videos:
        urls.append(start + (video['videoId']))     # getting the links of all the videos

    return urls


def title(url):
    yt = YouTube(url)       # getting titles      
    return yt.title


while True:
    old_list = links()  # getting all YT videos
    time.sleep(2700)  # waiting 45 mins
    extra = []
    updated = links()
    if updated != old_list:   # checking if new videos have been uploaded in 45 mins
        difference = len(updated) - len(old_list)      

        for i in range(difference):
            extra.append(updated[-(i + 1)])

        for i in range(len(extra)): 
            reddit.subreddit.submit(title(extra[i]), extra[i])     # uploading new videos
            time.sleep(900)
    else:
        continue
