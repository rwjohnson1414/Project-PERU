import praw
import time
from praw.models import MoreComments


start_time = time.time()
file = open("democrat_data.txt", "w")
data = []

# API Configuration: Apply Information below from Reddit to enable API
reddit = praw.Reddit(client_id=':^)',
                     client_secret=':^)',
                     user_agent='Project PERU',
                     username=':^)',
                     password=':^)')

# democratic subreddits
democrats = reddit.subreddit('democrats')
liberal = reddit.subreddit('Liberal')
socialism = reddit.subreddit('socialism')
feminism = reddit.subreddit('feminism')

dem_count = 0
for submission in democrats.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))
        dem_count += 1

lib_count = 0
for submission in liberal.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))
        lib_count += 1

soc_count = 0
for submission in socialism.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))
        soc_count += 1

fem_count = 0
for submission in feminism.hot(limit=50):
    submission.comment_sort = 'top'
    comments = submission.comments
    for comment in comments:
        if isinstance(comment, MoreComments):
            continue
        parsed_comment = comment.body
        data.append(parsed_comment.encode('utf-8'))
        fem_count += 1

i = 0
for element in data:
    file.write(str(i) + ".) " + element + "\n")
    i = i + 1

print "--- comments: " + str(i) + "---"
print "dem count: " + str(dem_count)
print "lib count: " + str(lib_count)
print "soc count: " + str(soc_count)
print "fem count: " + str(fem_count)
print "--- %s seconds ---" % (time.time() - start_time)
