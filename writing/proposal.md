# Proposal for Da Discretes

After thinking of multiple ideas, we have narrowed down our options to one
singular project. A lot of our project ideas surrounded music, and this one is
no different. Our original idea for this project was to create some sort of tune
for a give article. This broader idea was funneled down to having a song created
for a news article based on the tone of the words in the text. So, if the
article is sad or angry, the tone of this song will be slower or more of a lower
pitch. If the paper is happy, the song will reflect this by having a higher
pitches and more up tempo beats. This would be interesting to see what you can
expect of an article without ever reading any of its content.

This idea touches a few different areas of computer science. For one, some sort
of rudimentary sentiment analysis will need to be completed. A package such as
*gensim* will need to be used which allows you to perform sentiment analysis on
text data using python. We may not even need to use a package such as this. One
approach we could be taking is to make the pitch higher if the current word in
the paper is a 'good' word and lower the pitch if it is a 'bad' word. These
words could be determined using some sort of dataset full of al englis language
words where they are split into positive and negative words.

Finally, we will need to produce sounds. Luckily there is a package called music
in python which you can install just with using *pip install music*. This will
allow us to custom make sounds and music in python.
