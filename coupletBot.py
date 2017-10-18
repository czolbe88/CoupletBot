import praw
import couplet
import rhyme
import os
from datetime import datetime




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



for submission in subreddit3.new(
        limit=20):  # subreddit.new or any of the following: controversial, gilded, hot, rising, top,
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)

    submission.comment_sort = 'new'
    submission.comments.replace_more(limit=0)  # top level comment forests. iterable object
    for comment in submission.comments.list():
        print("comment: " + comment.body)
        print("author: " + str(comment.author))

        if str(comment.author) != "peacefulOcean":  # add condition, author is not peacefulocean
            strcomment = str(comment.body)
            testcouplet = couplet.coupletize(strcomment)

            if testcouplet != None:
                successful_couplets.append(testcouplet)  # append the output to successful_couplets
                author = str(comment.author)
                with open("couplets_found.txt", "a") as f:

                    f.write(  str(datetime.fromtimestamp(comment.created))  + "\n" + author + "\n\n" +
                             testcouplet + "\n\n" + "-----" +"\n\n" )



        print("--- End of Comment ---")

    '''for top_level_comment in submission.comments :
        nombor =1
        print("comment no." + str(nombor) + ": " + top_level_comment.body)
        nombor+=1
        top_level_comment.reply("testing")'''

    print(" --------- End of Submission ---------\n")

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
