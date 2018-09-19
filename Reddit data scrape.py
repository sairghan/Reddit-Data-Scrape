
import pandas as pd
import datetime as dt
import praw
import json

reddit = praw.Reddit(client_id='*************',                      
                     client_secret='******************',                      
                     user_agent='**********',                      
                     username='***********',                      
                     password='*********')


subreddit = reddit.subreddit('all')
stream_subreddit = subreddit.search("student visa")


records_dict = {"subreddit":[],                
                "title":[],                
                "description":[],               
                "number of comments":[]}

comments_dict = {"comment":[]}

for submission in stream_subreddit:
    records_dict["subreddit"].append(submission.subreddit.display_name)
    records_dict["title"].append(submission.title)   
    records_dict["description"].append(submission.subreddit.description)
    records_dict["number of comments"].append(submission.num_comments)
    if submission.num_comments > 0:
        for top_level_comment in submission.comments:
            comments_dict["comment"].append(top_level_comment.body)


records_data = pd.DataFrame(records_dict)
comments_data = pd.DataFrame(comments_dict)

with open('FileA.json', 'w') as fp:
    fp.write(records_data.to_json(orient='records'))

with open('FileB.json', 'w') as fp:
    fp.write(comments_data.to_json(orient='records'))

