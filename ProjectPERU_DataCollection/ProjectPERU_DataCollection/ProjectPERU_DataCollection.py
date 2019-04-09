import praw 

#API Configuration: Apply Information below from Reddit to enable API
reddit = praw.Reddit(client_id='iPfvVyGHka22BA',
                     client_secret='ed6HNahtptNuldBkduE_up753as',
                     user_agent='Python Political Predictor by /u/Snazlie',
                     username='**************',
                     password='**************')

print reddit.read_only
print reddit.user.me()
