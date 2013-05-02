import wikidown
import re
import os
import sys
import markov


WORD_RE = r'^[a-zA-Z][a-zA-Z-\']*$'


def words(body):
    for word in body.split():
        word = word.strip(' ,.[]')
        if re.match(WORD_RE, word):
            yield word


def main():
    mkv = markov.make_markov()
    page = wikidown.GetWikipediaPage(sys.argv[1])
    markov.feed_markov(mkv, words(page['content']))

    w = markov.walk_markov(mkv)
    for i in xrange(500):
        print w.next(),


if __name__ == '__main__':
    main()
