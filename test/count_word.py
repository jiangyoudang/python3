#! /usr/bin/python3

import doctest
import heapq


def freq_words(text, k):
    '''
    >>> freq_words(' ', 2)
    []
    >>> freq_words('If it\\n contains\\t other word delimitations other than space, it will work as well', 2)
    ['it', 'other']
    >>> freq_words(' One Two Three 3 Three 3 2 Two 1 3 Three', 5)
    ['3', 'Three', 'Two', '1', '2']

    :param text: a String representing a text document
    :param k: an integer providing the number of items to return
    :return: a list of Strings ordered by word frequency, the most frequently occurring word first
    '''

    # Time complexity is O(n)
    count_dict = {}
    words = text.split()

    # count frequency of each word using hash table
    # with time Complexity of O(n)
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

    # get k result using heap
    # with time complexity O(k*lgn)
    result = []
    heap = []
    for word, count in count_dict.items():
        heapq.heappush(heap, (-count, word))

    # get result for output
    if k > len(heap):
        k = len(heap)
    for i in range(k):
        curr = heapq.heappop(heap)
        result.append(curr[1])

    return result

if __name__ == "__main__":
    doctest.testmod()
