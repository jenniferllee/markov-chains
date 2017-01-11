from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    open_file = open(file_path).read()
    # print type(green_eggs_file)

    return open_file


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    words = text_string.split()
    chains = {}

    for i in range(len(words)-n):
        key = []
        for j in range(n):
            key = key + [words[j+i]]
        value = words[i+j+1]
        ngram = tuple(key)
        #print ngram

    # for i in range(len(words) - int(n)):
    #     key = []
    #     for j in range(n):
    #         key = key + [words[j+i]]
    #         #key2 = words[i + 1]
    #     value = words[i + j + 1]
    #     ngram = tuple(key)
    #     print ngram

        # if bigram in chains:
        #     chains[bigram].append(value)
        # else:
        #     chains[bigram] = [value]
        chains[ngram] = chains.get(ngram, []) + [value]
        # chains[bigram].append(value)
    #print ngram

    #print chains
    return chains

def initial_key(chains_dict, n):
    """ Creates a random key from a given dictionary. Outputs a tuple of length n
    """

    random_key = choice(chains_dict.keys()) #tuple
    while not random_key[0][0].isupper():
        random_key = choice(chains_dict.keys())

    return random_key

def make_text(chains_dict, n):
    """Takes dictionary of markov chains; returns random text."""

    # your code goes here

    text = ""
    # final_text = ""
    #pick random key which is a tuple of size n
    
    random_key = initial_key(chains_dict, n)
    for word in random_key:
    text = text + ' ' + word + ' '

    random_value = choice(chains_dict[random_key]) #one word


    text = text + random_value



    new_key_list = list(random_key[1:]) + [random_value]
    new_key = tuple(new_key_list)
    # print new_key

    while new_key in chains_dict:
        random_value = choice(chains_dict[new_key])
        text = text + ' ' + random_value + ' '
        new_key_list = list(new_key[1:]) + [random_value]
        new_key = tuple(new_key_list)
    return text

    # return final_text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains, int(sys.argv[2]))

print random_text
