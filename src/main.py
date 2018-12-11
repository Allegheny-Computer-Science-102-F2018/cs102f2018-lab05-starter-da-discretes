import re
import pygame
import time


def get_positive():
    positive_file = "../data/positive-words.txt"
    with open(positive_file, 'r') as positive_words:
        for line in positive_words:
            yield line.replace("\n","")

def get_negative():
    negative_file = "../data/negative-words.txt"
    with open(negative_file, 'r') as negative_words:
        for line in negative_words:
            yield line.replace("\n","")

def is_stop_word(new_word):
    file = "../data/stop_words.txt"
    with open(file, 'r') as stop_words:
        for word in stop_words:
            if new_word == word.strip().replace("\n",""):
                return True
    return False

def get_article_contents(file_name):
    file_name = "../input/%s" % (file_name)
    words = []
    with open(file_name, 'r') as article_contents:
        for line in article_contents:
            for word in line.split(" "):
                new_word = re.sub(r'[^a-zA-Z]', '', word).strip().replace("\n","").lower()
                if new_word and not is_stop_word(new_word):
                    words.append(new_word)
    return words

def readWAV(*audio_files, positive_tone, negative_tone):

    audios = ["sounds/"+str(i) for i in audio_files]

    avg_tone = positive_tone / (positive_tone + negative_tone)
    ind_to_play = int(len(audios) * avg_tone)

    if (ind_to_play >= len(audios)):
        ind_to_play = len(audios) - 1

    print("Avg of tone = ", avg_tone)
    print("Length of audios = ", len(audios))
    print("Index to play = ", ind_to_play)

    pygame.init()

    pygame.mixer.music.load("sounds/"+audio_files[ind_to_play])

    pygame.mixer.music.play()

    time.sleep(10)

def main(article):
    positive_tone = 0
    negative_tone = 0

    article_contents = get_article_contents(article)

    for word in article_contents:
        for pos_word, neg_word in zip(get_positive(), get_negative()):
            if word == pos_word:
                positive_tone = positive_tone + 1
                break
            if word == neg_word:
                negative_tone = negative_tone + 1
                break

    print("Positive Tone = ",positive_tone)
    print("Negative Tone = ",negative_tone)

    audio_files = ("negative1.wav", "negative2.wav", "negative3.mp3", "negative4.wav", "positive1.wav",  "positive2.wav",  "positive3.wav",  "positive4.wav",  "positive5.wav")
    readWAV(*audio_files, positive_tone = positive_tone, negative_tone = negative_tone)

# Main method invocation
if __name__ == "__main__":
    main("test_article.txt")