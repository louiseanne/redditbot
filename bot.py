import praw
import random
import datetime
import time

# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "AOC is so [COOL], I heard she [GOOD_DEED] [DAY_PAST] at a [PLACE] in [CITY]. And it wasn't even for a photo op!",
    "AOC will be [DOING] at [SCHOOL] to celebrate the grauation of students majoring in [MAJOR1]. Even though she won't be speaking to students majoring in [MAJOR3], I still think AOC is [ADJ] [COOL]",   
    "When AOC runs for president in [ELECTION_YEAR], she's going to appoint [CELEBRITY] to be vice president. AOC said '[CELEBRITY] is [ADJ] [COOL]', you should [ACTION] for AOC today.",
    "[DAY_PAST], AOC [GOOD_DEED]. When AOC runs for president in [ELECTION_YEAR], she's going to [DO]. America needs someone to [DO]. [ACTION] for AOC today to be a [COOL] [ANIMAL].",
    "Did you know that AOC's favorite animal is a [ANIMAL]? She's so [ADJ] [COOL]! If you like [ANIMAL]s, you should [ACTION] for AOC. If you don't, you should change your [BAD_ADJ] opinion.",
    "Only [BAD_ADJ] [PEOPLE] hate AOC. Don't be like the [BAD_ADJ] [PEOPLE]. [ACTION] for AOC today to be a [COOL] [ANIMAL]."
    ]

replacements = {
    'SCHOOL' : ['Scripps', 'Claremont Mckenna', 'Harvey Mudd', 'Pitzer', 'Pomona'],
    'CITY' : ['Claremont', 'Constantinople', 'Atlantis', 'New Amsterdam', 'Hogsmeade', 'Twin Peaks', 'Gotham City'],
    'PEOPLE' : ['cats', 'women', 'men', 'people', 'elephants', 'lizards', 'squirrels'],
    'GOOD_DEED' : ['saved a kitten', 'helped your mom carry in the groceries', 'kissed a baby (consentually)', 'gave a monkey a banana', 'ate a vegan burger instead of a regular burger'],
    'DO' : ['gatekeep', 'gaslight', 'girlboss'],
    'PLACE' : ['supermarket', 'hospital', 'dive bar', 'hair salon', 'cafe', 'furniture store'],
    'ADJ' : ['super duper', 'extra double', 'insanely', 'crazy'],
    'MAJOR1' : ['underwater basket weaving', 'mansplaining', 'manspreading', ],
    'MAJOR3' : ['goat milking', 'freestyle dentistry', 'unrequited love letter writing'],
    'CELEBRITY' : ['Taylor Swift', 'Adele', 'Ariana Grande', 'Lorde', 'Bruno Mars', 'John Stamos', 'Tom Holland', 'Zendaya', 'Dakota Johnson', 'Anya Taylor-Joy', 'Joe Jonas', 'Saoisse Ronan'],
    'ACTION' : ['vote', 'volunteer'],
    'DOING' : ['freestyle rapping', 'dancing', 'reading', 'speaking', 'coaching the football team', 'teaching a class'],
    'COOL' : ['cool', 'fantastic', 'fabulous', 'incredible'],
    'DAY_PAST' : ['yesterday', 'yesterday afternoon', 'yesterday morning', 'last night', 'last night at 12:37 am'],
    'ELECTION_YEAR' : ['2024', '2028', '2032', '2036'],
    'ANIMAL' : ['sloth', 'lizard', 'iguana', 'spider', 'bear', 'frog'],
    'BAD_ADJ' : ['nasty', 'boring', 'lazy', 'stupid']
}

import random
import praw
import time
reddit = praw.Reddit("bot1", user_agent='cs40bot')

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    sentence = random.choice(madlibs)
    for k in replacements.keys():
        sentence = sentence.replace('['+k+']', random.choice(replacements[k]))
    return sentence

def score_comment(comment):
    comment = random.choice(comments_without_replies)
    comment_score = comment.score
    return comment_score

# connect to reddit 
reddit = praw.Reddit("bot1", user_agent='cs40bot')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTownFriends/comments/r1eqwb/practice_post_sillyclassbot/'
#submission_url = 'https://old.reddit.com/r/BotTown/comments/qxokru/practice_6/'
submission = reddit.submission(url=submission_url)
#print('home submission', submission)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()


    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.

    print('len(all_comments)=',len(all_comments))

    # (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        #print('comment.author', type(comment.author))
        #print('type(comment.author)=', type(comment.author))
        if str(comment.author) != 'silly-classbot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented is True:
        # (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)
    
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            have_we_replied = False
            for reply in comment.replies: #make a determination of if there is reply or no
                if str(reply.author) == 'silly-classbot':
                    have_we_replied = True
            if have_we_replied == False:
                comments_without_replies.append(comment)
                #print('what comment', comment.author)
                #print('what reply', reply.author)
                #else:
                    #not_my_comments = not_my_comments.remove(comment)
                    
                    
        #print("comments_without_replies=", len(comments_without_replies))
        #THIS IS INCORRECT


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        #print('authors of comments without', [comment.author for comment in comments_without_replies])
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message


        try:
            #comment = random.choice(comments_without_replies)
            comment = sorted(comments_without_replies, key=score_comment, reverse=True)[0]
            text = generate_comment()
            comment.reply(text)
            print(comment.author)
        except praw.exceptions.APIException:
            print('not replying to a comment that has been deleted')
        except IndexError:
            print('not replying to a post where ive already replied and commented on everything')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    # submission = random.choice(in here)
    #subreddit = reddit.subreddit("BotTown")
    #print(list(reddit.subreddit("BotTown").hot(limit=5)))
    submission = random.choice(list(reddit.subreddit("BotTownFriends").hot(limit=5)))
    print(submission)

    #^^ add sum in random.choice

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(30)