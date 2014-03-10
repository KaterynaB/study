"""Print n most frequent words and count from file with count."""

import sys
import operator
import collections


def get_words_from_file(path):
    """Extracts words from file.

    Args:
      path: string representing path to file.

    Yields:
      string representing a word extracted from the file.
    """
    with open(path, 'r') as words_file:
        for line in words_file:
            words = line.split()
            for word in words:
                yield word

def get_most_freq_words(path, n):
    """Gets n most frequent words with count.

    Words are read from the file.

    Args:
      path: string representing path to file.
      n: integer indicating how many words should be included in the result.

    Returns:
      list of tuples mapping word to it's count within the file. For example
      [('white', 2), ('a', 2), ('shot', 1)].
    """
    words_count = collections.defaultdict(int)
    for word in get_words_from_file(path):
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
