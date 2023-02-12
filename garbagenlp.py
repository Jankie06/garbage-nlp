from termcolor import colored as c
import requests
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import time
import string

# Text colors	Text highlights	Attributes
# black	        on_black	    bold
# red	        on_red	        dark
# green     	on_green	    underline
# yellow	    on_yellow	    blink
# blue	        on_blue	        reverse
# magenta   	on_magenta	    concealed
# cyan	        on_cyan
# white	        on_white
# light_grey	on_light_grey
# dark_grey	    on_dark_grey
# light_red	    on_light_red
# light_green	on_light_green
# light_yellow	on_light_yellow
# light_blue	on_light_blue
# light_magenta	on_light_magenta
# light_cyan	on_light_cyan

# CC coordinating conjunction
# CD cardinal digit
# DT determiner
# EX existential there(like: “there is ” … think of it like “there exists”)
# FW foreign word
# IN preposition/subordinating conjunction
# JJ adjective – ‘big’
# JJR adjective, comparative – ‘bigger’
# JJS adjective, superlative – ‘biggest’
# LS list marker 1)
# MD modal – could, will
# NN noun, singular ‘- desk’
# NNS noun plural – ‘desks’
# NNP proper noun, singular – ‘Harrison’
# NNPS proper noun, plural – ‘Americans’
# PDT predeterminer – ‘all the kids’
# POS possessive ending parent’s
# PRP personal pronoun –  I, he, she
# PRP$ possessive pronoun – my, his, hers
# RB adverb – very, silently,
# RBR adverb, comparative – better
# RBS adverb, superlative – best
# RP particle – give up
# TO – to go ‘to’ the store.
# UH interjection – errrrrrrrm
# VB verb, base form – take
# VBD verb, past tense – took
# VBG verb, gerund/present participle – taking
# VBN verb, past participle – taken
# VBP verb, sing. present, non-3d – take
# VBZ verb, 3rd person sing. present – takes
# WDT wh-determiner – which
# WP wh-pronoun – who, what
# WP$ possessive wh-pronoun, eg - whose
# WRB wh-adverb, eg - where, when


URL = r"https://gist.githubusercontent.com/ZohebAbai/513218c3468130eacff6481f424e4e64/raw/b70776f341a148293ff277afa0d0302c8c38f7e2/gist_stopwords.txt"
currentToken = "ERROR: Unknown"
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def setup():
    global STOPWORDS

    # Display loading indicator and title
    print(c("Garbage ", "light_blue", attrs=["underline"])+c(
        "NLP", "light_cyan", attrs=["bold", "underline"])+c("\nLoading...", "dark_grey"))

    # Attempt to download stopwords list and format
    try:
        response = requests.get(URL)
        content = response.text
        STOPWORDS = content.split(",")
        # Get nltk libraries
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        # Clear and print success message
        os.system("cls")
        input(c("Garbage ", "light_blue", attrs=["underline"])+c(
            "NLP", "light_cyan", attrs=["bold", "underline"])+c("\nSuccess!", "green")+c("\nPress ", "light_green")+c("[ENTER]", "yellow", attrs=["dark", "bold"])+c(" to begin!", "light_green"))
    except:
        # Clear and print fail message
        os.system("cls")
        print(c("Garbage ", "light_blue", attrs=["underline"])+c(
            "NLP", "light_cyan", attrs=["bold", "underline"])+c("\nFailed!", "red")+c("\nAre you connected to the internet?", "light_red"))
        exit()  # Commit scooter ankle


def status(status):
    os.system("cls")
    if status != "null":
        return c("Garbage ", "light_blue", attrs=["underline"])+c(
            "NLP", "light_cyan", attrs=["bold", "underline"])+c(f" • {status}", "dark_grey")
    else:
        return c("Garbage ", "light_blue", attrs=["underline"])+c(
            "NLP", "light_cyan", attrs=["bold", "underline"])


def userInput():
    global currentToken

    # Update status
    print(status("Getting user input..."))

    # Set token to user response
    currentToken = input(
        c("[", "white")+c("YOU", "light_green", attrs=["bold"])+c("] > ", "white"))


def segmentation():
    global currentToken

    # Update status
    print(status("Segmenting words..."))

    # Split words
    currentToken = currentToken.lower().translate(
        str.maketrans('', '', string.punctuation)).split()


def stopwords():
    global currentToken, STOPWORDS

    # Update status
    print(status("Removing words..."))

    # Check for words in stoplist
    for i in currentToken:
        if i in STOPWORDS:
            currentToken.remove(i)
    print(currentToken)


def stem():
    global currentToken

    # Update status
    print(status("Stemming words..."))

    # Convert words into simple form
    for i in currentToken:
        index = currentToken.index(i)
        replace = ps.stem(i)
        replace = lemmatizer.lemmatize(replace)
        currentToken[index] = replace


def tag():
    global currentToken

    # Update status
    print(status("Tagging words..."))

    # Add tags and identifiers
    currentToken = nltk.pos_tag(currentToken)
    print(currentToken)
    # TODO Print specific identiyer!
    print(currentToken[0][1])
    time.sleep(20)


def mainLoop():
    # Clear
    os.system("cls")

    # Phase 1: Get user input
    userInput()

    # Phase 2: Separate words and tokenize
    segmentation()

    # Phase 3: Remove unimportant words
    stopwords()

    # Phase 4: Simplify words
    stem()

    # Phase 5: Tag words
    tag()


# ---------------------------------  Program Start  --------------------------------- #
setup()

# Program Loop
while True:
    mainLoop()
