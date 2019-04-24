import praw 
import time

start_time = time.time()
repFile = open("republicanData.txt","w")
demFile = open("democraticData.txt","w")
republicanData = []
democraticData = []

#API Configuration: Apply Information below from Reddit to enable API
reddit = praw.Reddit(client_id='iPfvVyGHka22BA',
                     client_secret='ed6HNahtptNuldBkduE_up753as',
                     user_agent='Python Political Predictor by /u/Snazlie',
                     username='Snazlie',
                     password='***********************************')

#republican subreddits
republicans = ['Republican','Conservative','The_Donald','askaconservative']
democrats = ['democrats','Fuckthealtright','Liberal','feminism']

for subreddit in republicans:
    sub = reddit.subreddit(subreddit)
    for submission in sub.hot(limit=50):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=750)
        for comment in submission.comments:
            parsed_comment = comment.body
            republicanData.append(parsed_comment.encode('utf-8'))

for subreddit in democrats:
    sub = reddit.subreddit(subreddit)
    for submission in sub.hot(limit=50):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=750)
        for comment in submission.comments:
            parsed_comment = comment.body
            democraticData.append(parsed_comment.encode('utf-8'))


rCount = 0
for element in republicanData:
    repFile.write(str(rCount) + ".) " + element + "\n")
    rCount = rCount + 1

dCount = 0
for element in democraticData:
    demFile.write(str(dCount) + ".) " + element + "\n")
    dCount = dCount + 1

print "--- %s seconds ---" % (time.time() - start_time)
      