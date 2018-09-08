#!/usr/bin/python

import string
from random import shuffle

# Create the raw text to be worked with
raw_text = "Hello and welcome to Linux Academy!!"
print "This is my raw text: %s" % (raw_text)
letters = list(string.ascii_letters)

# Encode the letters
encoded_letters = letters[:]
# Shuffle the letters
shuffle(encoded_letters)

# Create the encoding/decoding keys - The hard way
#encoding_key = {}
#decoding_key = {}
#for k, v in zip(letters, encoded_letters):
#	encoding_key[k]=v
#	decoding_key[v]=k
#
#encoded_text = ''
#for letter in raw_text:
#	encoded_text += encoding_key.get(letter, letter)
#print encoded_text

# Smarter way to create the encoding/decoding keys
encoding_key = dict(zip(letters,encoded_letters))
decoding_key = dict(zip(encoding_key.values(),encoding_key.keys()))
encoded_text = ''.join([ encoding_key.get(w, w) for w in raw_text])
print "This is my encoded text: %s" % (encoded_text)

decoded_text = ''.join([ decoding_key.get(w, w) for w in encoded_text])
print "This is my decoded text: %s" % (decoded_text)