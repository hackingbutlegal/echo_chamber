# echo-chamber
A Python Script for #BlackLivesMatter and Other Important Topics

**Hi! 👋🏽**

I wrote a little tool in Python to either greatly improve your Twitter signal-to-noise ratio or strengthen your echo chamber, depending on how you look at it.

![](https://media.giphy.com/media/3o85xIO33l7RlmLR4I/giphy.gif)

**How it works:**

* It downloads the lists of people you follow & who follow you
* Checks to see if they've tweeted using the #BlackLivesMatter hashtag
* If they haven't, it sends them a Direct Message
* If they have, it sends them a different DM
* Gives you a summary report when complete

![](/uploads/screen-shot-2020-06-05-at-1-37-38-am.png)

**Future planned improvements:**

* Add rate limiting!! ASAP
* Want to add the option of unfollowing people who haven't
* Want to add the option of soft-blocking followers who haven't
* Stop writing to local files, handle data in memory
* Improve OS compatibility (so that it will run on Windows)

![](/uploads/screen-shot-2020-06-05-at-1-19-12-am.png)

**How to use:**

* Create an application and [generate](https://developer.twitter.com/) Twitter API keys
* Download .py from [Github](https://github.com/find-evil/echo-chamber)
* pip install twitter
* pip install dictor
* Edit the following variables:
  * Twitter API key placeholders
  * your_username - Your Twitter account's username
  * str1 - The string you want to search for.
  * msg_disappoint - What you send to those who haven't tweeted that string (there are two of these)
  * msg_thanks - What you send to those who have (there are also two of these)

Finally, run the code like this:

    python3 echo-chamber.py

![](/uploads/screen-shot-2020-06-05-at-3-08-39-am.png)

For some light added reading, [this article](https://www.insidescience.org/news/visualizing-twitter-echo-chambers) has interesting things to say on the topic of Twitter's echo chambers.

> The researchers found that while an overall consensus is possible, echo chambers could cause the discussion to destabilize and become polarized if the topic meets a certain level of controversy.
>
> Once a discussion is polarized, subsequent exchange of information would strengthen the echo chambers and drive the two groups further apart.

**Food for thought.**

Thanks to [Mike Verdone](https://mike.verdone.ca/twitter/) and the [Python Twitter Tools](https://github.com/sixohsix/twitter) developer team.
