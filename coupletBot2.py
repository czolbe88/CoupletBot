#!/usr/bin/python3.5
import sys
sys.path.append('\\home\\ubuntu\\.local\\lib\\python3.5\\site-packages')
sys.path.append('\\home\\ubuntu\\nltk_data\\corpora')
import praw
import couplet
import couplet2
import rhyme
import os
from datetime import datetime
import re




reddit = praw.Reddit('koopacopabot')

subreddit = reddit.subreddit("pythonforengineers")
subreddit2 = reddit.subreddit("reddit_bot_test")
subreddit3 = reddit.subreddit("singapore")

multireddit = [subreddit3]
all = reddit.subreddit("all")

signature = "This (uncalled for) couplet conversion service was provided by a bot"

# Submissions have a comments attribute that is a CommentForest instance.
# That instance is iterable and represents the top-level comments of the submission by the default comment sort (best)
successful_couplets = []



for submission in all.hot(
        limit=20):  # subreddit.new or any of the following: controversial, gilded, hot, rising, top,
    '''print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)'''

    submission.comment_sort = 'new'
    submission.comments.replace_more(limit=0)  # top level comment forests. iterable object

    with open("coupletserial.txt", "r") as coupletserial: # open verse serial file
        serials = coupletserial.read()

    for comment in submission.comments.list():
        '''print("comment: " + comment.body)
        print("author: " + str(comment.author))'''

        if str(comment.author) != "peacefulOcean":  # add condition, author is not peacefulocean
            strcomment = str(comment.body)
            testcouplet = couplet2.couplet(strcomment) #this is a list

            if testcouplet is not None:

                for verse in testcouplet:
                    author = str(comment.author)
                    with open(".\\couplets_found2.txt", "a") as f:

                        if re.search( (str(datetime.fromtimestamp(comment.created)) + author), serials) is None: # ensure that this verse has not been recorded

                            f.write(  str(datetime.fromtimestamp(comment.created))  + "\n" + author + "\n\n" +
                                     verse + "\n\n" + "-----" +"\n\n" )

                            with open(".\\coupletserial.txt", "a") as g:
                                g.write(str(datetime.fromtimestamp(comment.created)) + author ) #give the verse a serial number





        #print("--- End of Comment ---")

    '''for top_level_comment in submission.comments :
        nombor =1
        print("comment no." + str(nombor) + ": " + top_level_comment.body)
        nombor+=1
        top_level_comment.reply("testing")'''

    #print(" --------- End of Submission ---------\n")

'''
 dir(submission)

['approve',
'approved_by',
'author',

'domain',
'downs',
'downvote',
'edit',
'edited',

'saved',

'score',
'secure_media',
'secure_media_embed',
'selftext',
'selftext_html',

'title',

'ups',
'upvote',
'url',
'user_reports',
'visited',
'vote']

'''
