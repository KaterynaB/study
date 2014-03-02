"""Print n most frequent words and count from file with count."""

import sys
import operator
import collections

def get_most_freq_words(path, n):
    # Build dict where keys are words and
    # values are corresponding word counts.
    f = open(path, 'r')
    words_count = collections.defaultdict(int)
    for line in f:
        words = line.split()
        for word in words:
            words_count[word] += 1

    # Return n most frequently used words.
    words_and_counts = words_count.items()
    words_and_counts.sort(key=operator.itemgetter(1), reverse=True)
    return words_and_counts[:n]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        n = int(sys.argv[2])
    elif len(sys.argv) == 2:
        n = 3
    else:
        # this is error case so we exit with non zero status
        print "Please provide arguments"
        exit(-1)

    print get_most_freq_words(sys.argv[1], n)
