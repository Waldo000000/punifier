#!/usr/bin/python
"""
Punifier
"""
import sys
from sets import Set
import nltk
import argparse

# TODO: parse from args
#text = "'I like bikes!' said Rob.";

# TODO
thesaurus = { 
  "said": ["spoke"],
  "spoke": ["said"],
};

# TODO
def getTopicWords(topic):
  if (topic == "bikes"):
    return [ "spoke", "tired" ];
  return [];

def getTopic(text):
  # TODO
  return "bikes";

def replaceTokens(text, topicWords, thesaurus):
  result = [];
  tokens = nltk.word_tokenize(text);
  for token in tokens:
    synonyms = thesaurus.get(token)
    if synonyms:
      candidates = list(set(synonyms) & set(topicWords)) # TODO: optimize if necc. 
      if candidates:
        result.append(candidates[0].upper()) # TODO: score candidates
        continue
    result.append(token)
  return ' '.join(join_punctuation(result))

def punify(text):
  topic = getTopic(text);
  topicWords = getTopicWords(topic);
  return replaceTokens(text, topicWords, thesaurus);

def main(): 
  parser = argparse.ArgumentParser()
  parser.add_argument('infile', type=argparse.FileType('r'))
  args = parser.parse_args()

  for line in args.infile:
    print punify(line);

# TODO: fix joining of tokens
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
