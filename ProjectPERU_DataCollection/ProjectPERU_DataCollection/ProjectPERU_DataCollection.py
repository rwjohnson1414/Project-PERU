import praw 
import time

start_time = time.time()
file = open("data.txt","w")
data = []

#API Configuration: Apply Information below from Reddit to enable API
reddit = praw.Reddit(client_id='iPfvVyGHka22BA',
                     client_secret='ed6HNahtptNuldBkduE_up753as',
                     user_agent='Python Political Predictor by /u/Snazlie',
                     username='*****************************',
                     password='*****************************')

#republican subreddits
republican = reddit.subreddit('Republican')
conservative = reddit.subreddit('Conservative')
theDonald = reddit.subreddit('The_Donald')
askAConserative = reddit.subreddit('askaconservative')

for submission in republican.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))

for submission in conservative.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))

for submission in theDonald.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments: 
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))

for submission in askAConserative.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments: 
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))

i = 0
for element in data:
    file.write(str(i) + ".) " + element + "\n")
    i = i + 1

print "--- %s seconds ---" % (time.time() - start_time)
      