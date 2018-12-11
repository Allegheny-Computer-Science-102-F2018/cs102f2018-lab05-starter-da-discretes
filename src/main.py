import re
import pygame
import time


# Date = 11 December 2018
# Version = 1
# Original Author = Austin Bristol, Karol Vargas, David Perez, Francisco Guzman
# Description: Program that plays a sound file based on the sentiment of an article


def get_positive():
    """
    This function is a generator. Each time the generator gets called for the
    next iteration, we get the next word from the file and return it. This is so
    that we don't store the thousands of words in a python list, but rather only
    get the words when we need them.
    """

    positive_file = "../data/positive-words.txt" # Name of positive word file
    with open(positive_file, 'r') as positive_words: # Open file
        for line in positive_words: # Read each line in file
            yield line.replace("\n","") # Return the current word when asked to


def get_negative():
    """
    This function is a generator. Each time the generator gets called for the
    next iteration, we get the next word from the file and return it. This is so
    that we don't store the thousands of words in a python list, but rather only
    get the words when we need them.
    """

    negative_file = "../data/negative-words.txt" # Name of negative word file
    with open(negative_file, 'r') as negative_words: # Open file
        for line in negative_words: # Read each line in file
            yield line.replace("\n","") # Return the current word when asked to


def is_stop_word(new_word):
    """
    This function takes the input word and returns true if it is a stop word; a
    word we do not want.
    """

    file = "../data/stop_words.txt" # Name of stop word file
    with open(file, 'r') as stop_words: # Open file
        for word in stop_words: # Read each word in file
            if new_word == word.strip().replace("\n",""): # Current word matches
                return True # Return that it is a stop word
    return False # We got through all of the words without any matches

def get_article_contents(file_name):
    """
    This function will iterate over the input article. It will return a list of
    words with symbols, numbers, and stop words filtered out.
    """

    file_name = "../input/%s" % (file_name) # Gets the path to the article
    words = [] # Declares an empty words list
    with open(file_name, 'r') as article_contents: # Opens file
        for line in article_contents: # Iterate over each line
            for word in line.split(" "): # Iterate over each word in line

                # Filter out numbers, symbols, and new lines. Also lower case everything.
                new_word = re.sub(r'[^a-zA-Z]', '', word).strip().replace("\n","").lower()

                # Don't keep word if it is a stop word or if it is empty.
                if new_word and not is_stop_word(new_word):
                    words.append(new_word) # Add word to the list

    return words # Return list of words

def readWAV(*audio_files, positive_tone, negative_tone):
    """
    This function takes a variable amount of parameters for audio files. Also,
    we take parameters for positive and negative tones. We select a correct
    sound to play, and actually play it.
    """

    # Manipulate list into correct file paths
    audios = ["sounds/"+str(i) for i in audio_files]

    # Calculate average positive tone of article
    avg_tone = positive_tone / (positive_tone + negative_tone)

    # Get an index of the song based on sentiment
    ind_to_play = int(len(audios) * avg_tone)

    # If 100% positive, we need to subtract by 1 to get last index.
    if (ind_to_play >= len(audios)):
        ind_to_play = len(audios) - 1

    # Print debug information
    print("Avg of tone = ", avg_tone)
    print("Length of audios = ", len(audios))
    print("Index to play = ", ind_to_play)

    # Initialize pygame game
    pygame.init()

    # Load the correct song that we want to play
    pygame.mixer.music.load(audios[ind_to_play])

    # Play song
    pygame.mixer.music.play()

    # Wait for song to finish
    time.sleep(10)

def main(article):
    """
    Main function which runs all the code and calls the rest of the functions.
    Takes in the file name for the article that you placed in the input folder.
    """

    # Initialize tones
    positive_tone = 0
    negative_tone = 0

    # Get article contents
    article_contents = get_article_contents(article)

    # Iterate over each meaningful word in article
    for word in article_contents:
        # iterate over the positive/negative word generators
        for pos_word, neg_word in zip(get_positive(), get_negative()):
            # If it is a positive word add to the tone and break
            if word == pos_word:
                positive_tone = positive_tone + 1
                break
            # If it is a negative word add to the tone and break
            if word == neg_word:
                negative_tone = negative_tone + 1
                break

    # Print debug results
    print("Positive Tone = ",positive_tone)
    print("Negative Tone = ",negative_tone)

    # Tuple of audio files in the sounds directory
    audio_files = ("negative1.wav", "negative2.wav", "negative3.mp3", "negative4.wav", "positive1.wav",  "positive2.wav",  "positive3.wav",  "positive4.wav",  "positive5.wav")

    # Actually play the output
    readWAV(*audio_files, positive_tone = positive_tone, negative_tone = negative_tone)

# Main method invocation
if __name__ == "__main__":
    main("test_article.txt")
