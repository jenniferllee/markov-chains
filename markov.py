from random import choice
import random


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    open_file = open(file_path).read()
    # print type(green_eggs_file)

    return open_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()
    chains = {}     #dictionary
    for i in range(len(words) - 2):
        key1 = words[i]
        key2 = words[i + 1]
        value = words[i + 2]
        bigram = (key1, key2)
        if bigram in chains:
            chains[bigram].append(value)
        else:
            chains[bigram] = [value]

    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    first_bigram = random.choice(chains.key())
    word1 = first_bigram[0]
    word2 = first_bigram[1]
    word3 = random.choice(chains[first_bigram])
    text = text + "%s %s %s" % (word1, word2, word3)
    new_key = (word2, word3)

    while new_key in chains:
        word1 = new_key[0]
        word2 = new_key[1]
        word3 = random.choice(chains[new_key])
        text = text + "%s %s %s" % (word1, word2, word3)
        new_key = (word2, word3)

        print text

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
