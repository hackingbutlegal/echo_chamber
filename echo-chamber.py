# https://github.com/find-evil/echo-chamber
# https://jackie.lol/posts/presenting-echo-chamber-a-python-tool-for-blacklivesmatter/

import os
import json
from twitter import OAuth, Twitter

# REPLACE THESE PLACEHOLDERS WITH YOUR TWITTER API KEYS
t = Twitter(
    auth=OAuth('token', 'token_secret', 'consumer_key', 'consumer_secret'))

# SET YOUR TWITTER USERNAME HERE
your_username = "username"

# SET YOUR SEARCH TERM HERE
HASHTAG = "#BlackLivesMatter"

# OUTPUT LISTS
did_tweet = list()
did_not_tweet = list()
could_not_send_dm = list()

# GET LIST OF PEOPLE YOU FOLLOW
os.system('twitter-follow -o -g '+ your_username + '> tw_following.txt')
followingList = list()
with open("tw_following.txt", "r") as myfile:
    for line in myfile:
        followingList.append(line.strip())

# GET LIST OF PEOPLE WHO FOLLOW YOU
os.system('twitter-follow -o -r '+ your_username + '> tw_followers.txt')
followerList = list()
with open("tw_followers.txt", "r") as myfile:
    for line in myfile:
        followerList.append(line.strip())

# ITERATE THROUGH USERS YOU FOLLOW
for line in followingList:

    # STRIP UNNECESSARY CHARACTERS
    line = line[2:-1]

    # DM TEMPLATES
    MSG_DISAPPOINT = "Hi {tweep}. I've noticed you haven't directly tweeted in support of #BlackLivesMatter. It's really important. Please consider doing so.".format(tweep=line)
    MSG_THANKS = "Hi {tweep}. I just wanted to thank you personally for supporting #BlackLivesMatter. Thank you.".format(tweep=line)

    # QUERY THE API WITH PROPER FORMATTING
    query = t.search.tweets(q="from:{} {} ".format(line, HASHTAG), tweet_mode='extended')

    with open('tw_tweets.json', 'w') as f:
        json.dump(query, f)
    with open('tw_tweets.json') as data:
        data = json.load(data)
        tw_statuses = len(data['statuses'])
        # print(tw_statuses)
    if tw_statuses > 0:
        # print(MSG_THANKS)

        # APPEND USERNAMES TO THE did_tweet LIST
        did_tweet.append(line)

        try:
            t.direct_messages.events.new(
                _json={
                    "event": {
                        "type": "message_create",
                        "message_create": {
                            "target": {
                                "recipient_id": t.users.show(screen_name=line)["id"]},
                            "message_data": {
                                "text": MSG_THANKS}}}})
        except IOError:
            could_not_send_dm.append(line)

    else:
        # print(MSG_DISAPPOINT)

        # APPEND USERNAMES TO THE did_not_tweet LIST
        did_not_tweet.append(line)

        try:
            t.direct_messages.events.new(
                _json={
                    "event": {
                        "type": "message_create",
                        "message_create": {
                            "target": {
                                "recipient_id": t.users.show(screen_name=line)["id"]},
                            "message_data": {
                                "text": MSG_DISAPPOINT}}}})
        except IOError:
            could_not_send_dm.append(line)

# ITERATE THROUGH USERS WHO FOLLOW YOU
for line in followerList:

    # STRIP UNNECESSARY CHARACTERS
    line = line[2:-1]

    # DM TEMPLATES
    MSG_DISAPPOINT = "Hi {tweep}. I've noticed you haven't directly tweeted in support of #BlackLivesMatter. It's really important. Please consider doing so.".format(tweep=line)
    MSG_THANKS = "Hi {tweep}. I just wanted to thank you personally for supporting #BlackLivesMatter. Thank you.".format(tweep=line)

    # QUERY THE API WITH PROPER FORMATTING
    query = t.search.tweets(q="from:{} {} ".format(line, HASHTAG), tweet_mode='extended')
    with open('tweets.json', 'w') as f:
        json.dump(query, f)
    with open('tweets.json') as data:
        data = json.load(data)
        tw_statuses = len(data['statuses'])
    if tw_statuses > 0:
        # print(MSG_THANKS)

        if line not in did_tweet:
            try:
                t.direct_messages.events.new(
                    _json={
                        "event": {
                            "type": "message_create",
                            "message_create": {
                                "target": {
                                    "recipient_id": t.users.show(screen_name=line)["id"]},
                                "message_data": {
                                    "text": MSG_THANKS}}}})
            except IOError:
                could_not_send_dm.append(line)

            # APPEND USERNAMES TO THE did_tweet LIST
            did_tweet.append(line)

    else:
        # print(MSG_DISAPPOINT)

        if line not in did_not_tweet:
            try:
                t.direct_messages.events.new(
                    _json={
                        "event": {
                            "type": "message_create",
                            "message_create": {
                                "target": {
                                    "recipient_id": t.users.show(screen_name=line)["id"]},
                                "message_data": {
                                    "text": MSG_DISAPPOINT}}}})
            except IOError:
                could_not_send_dm.append(line)

            # APPEND USERNAMES TO THE did_not_tweet LIST
            did_not_tweet.append(line)

# OUTPUT RESULTS
print("\nSummary:")
print("\nThe following users tweeted your search term:")
print(did_tweet)
print("\nThe following users did not tweet your search term:")
print(did_not_tweet)
print("\nYou failed to send a DM to the following users (probably a 403):")
print(could_not_send_dm)
print("\nProcess Complete.")

# CLEANUP
os.system('rm tw_following.txt')
os.system('rm tw_followers.txt')
os.system('rm tw_tweets.json')
