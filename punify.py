#!/usr/bin/python
"""
Punifier

Usage: ./punifier.py ./text.txt
"""
import sys
from sets import Set
import nltk
import argparse

# TODO
thesaurus = { 
  'said': ['spoke'],
  'spoke': ['said'],
};

# TODO
def getTopicalWords(tokens):
  bikeWords = [ 'spoke', 'tired' ];
  tokenSet = set(tokens)
  if 'bikes' in tokenSet:
    return bikeWords;
  return [];

def replaceTokens(tokens, topicalWords, thesaurus):
  for idx, token in enumerate(tokens):
    synonyms = thesaurus.get(token) or [token]
    candidates = list(set(synonyms) & set(topicalWords)) # TODO: optimize if necc. 
    outToken = candidates[0].upper() if candidates else token # TODO: score candidates
    tokens[idx] = outToken

def punify(text):
  tokens = nltk.word_tokenize(text);
  topicalWords = getTopicalWords(tokens);
  replaceTokens(tokens, topicalWords, thesaurus);
  return ' '.join(join_punctuation(tokens))

def main(): 
  parser = argparse.ArgumentParser()
  parser.add_argument('infile', type=argparse.FileType('r'))
  args = parser.parse_args()

  for line in args.infile:
    print punify(line);

# TODO: is there a better way to un-tokenize via nltk?
def join_punctuation(seq, characters='.,;?!\''):
  characters = set(characters)
  seq = iter(seq)
  current = next(seq)

  for nxt in seq:
    if nxt in characters:
      current += nxt
    else:
      yield current
      current = nxt

  yield current

if __name__ == "__main__":
  main()
