1.	Project title: 
Project: P.E.R.U. (Political Expressions of Reddit Users)

2.	Team Members: 
Vincent Zelinsky, Reese Johnson, and Ariann Chai

3.	Motivation:
  This project obtain reddit users of strong political lean through the political party subreddits (top 10 upvoted comments per post), create datasets using the identified left & right winged users’ comment histories, then train a classifier to classifier users of unknown political lean. 
  a.	We can use this to determine which way a particular commenter leans and whether or not they may have bias. 
  b.	We could also use this on a representative sample of all the users on a subreddit to determine the entire subreddit’s political lean.
  c.	This could also be used specifically on the moderators of a subreddit to determine whether or not they themselves have a bias.

4.	Brief Survey of existing tools: 
  a.	Adam Morrison created a visualization on the political leanings of subreddits based on their news sources. Our tool is different because it will be determining the political leanings of specific users based on their comment history.

5.	The main components:
  a.	Dataset & data collection:
    Our dataset will be users’ comments from the subreddits like r/liberal and r/conservative. We can pull these comments using the reddit api (PRAW) or a web scraper.
  b.	Data preprocessing:
    The data is text so preprocessing is not necessary.
  c.	Potential data mining techniques: 
    Classification - Regression  
  d.	Other tools?:
    Tensorflow or scikit-learn and tableau

6.	Potential work distribution:
  a.	Data collection: Reese
  b.	Classifier training: Ariann & Vincent
  c.	Data visualisation: Reese

7.	Potential challenges:
  a.	Data Quality 
    We are assuming that users with top posts in r/liberal are liberal and the same for r/conservative.
