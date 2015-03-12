

def make_trie(words):
    if words is None:
        raise TypeError('The input has to be a words list')

    root = {}

    for word in words:
        curr = root
        if words is None:
            continue
        for c in word:
            curr = curr.setdefault(c, {})
        curr.setdefault('$', '$')

    return root


def in_trie(trie, word):
    curr = trie
    for c in word:
        if c in curr:
            curr = curr[c]
        else:
            return False
    return '$' in curr



# words = ['b', 'abc', 'abd', 'bcd', 'abcd', '', ' ']
words = []
trie = make_trie(words)
print(trie)
print(in_trie(trie, 'abc'))
# print(in_trie(trie, None))