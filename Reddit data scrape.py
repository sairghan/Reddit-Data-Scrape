
# coding: utf-8

# In[55]:


import pandas as pd
import datetime as dt
import praw
import json


# In[56]:


reddit = praw.Reddit(client_id='QkZM2q1MMjOFlg',                      client_secret='GCe2EGkAFy3y377N124Il8C9KaE',                      user_agent='pasam',                      username='saikick153',                      password='rakesh153@')


# In[57]:


subreddit = reddit.subreddit('all')
stream_subreddit = subreddit.search("student visa")


# In[58]:


records_dict = {"subreddit":[],                "title":[],                "description":[],                "number of comments":[]}

comments_dict = {"comment":[]}


# In[59]:


for submission in stream_subreddit:
    records_dict["subreddit"].append(submission.subreddit.display_name)
    records_dict["title"].append(submission.title)   
    records_dict["description"].append(submission.subreddit.description)
    records_dict["number of comments"].append(submission.num_comments)
    if submission.num_comments > 0:
        for top_level_comment in submission.comments:
            comments_dict["comment"].append(top_level_comment.body)


# In[60]:


records_data = pd.DataFrame(records_dict)
comments_data = pd.DataFrame(comments_dict)


# In[61]:


with open('C:\Users\sai.ghanta\Documents\TaskA.json', 'w') as fp:
    fp.write(records_data.to_json(orient='records'))


# In[62]:


with open('C:\Users\sai.ghanta\Documents\TaskB.json', 'w') as fp:
    fp.write(comments_data.to_json(orient='records'))

