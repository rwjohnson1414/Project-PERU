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
                     password='Peanut1414$$')

#republican/democratic subreddits
republicans = ['Republican','Conservative','The_Donald','askaconservative']
democrats = ['democrats','Fuckthealtright','Liberal','feminism']

for subreddit in republicans:
    sub = reddit.subreddit(subreddit)
    for submission in sub.hot(limit=100):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=750)
        for comment in submission.comments:
            print comment
            parsed_comment = comment.body
            republicanData.append(parsed_comment.encode('utf-8'))

for subreddit in democrats:
    sub = reddit.subreddit(subreddit)
    for submission in sub.hot(limit=250):
        submission.comment_sort = 'top'
        submission.comments.replace_more(limit=1000)
        for comment in submission.comments:
            print comment
            parsed_comment = comment.body
            parsed_comment.replace('\n',' ')
            democraticData.append(parsed_comment.encode('utf-8'))


rCount = 0
for element in republicanData:
    element = element.replace(',','')
    repFile.write(' ,' + element.replace('\n','') + '\n')
    rCount = rCount + 1

dCount = 0
for element in democraticData:
    element = element.replace(',','')
    demFile.write(' ,' + element.replace('\n','') + '\n')
    dCount = dCount + 1

print "--- %s seconds ---" % (time.time() - start_time)
      