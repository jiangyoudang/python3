class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        line = {'words':[],'len':0}
        justified = []
        for word in words:
            if line['len']+len(line['words'])+len(word)>L:
                justified.append(line)
                line = {'words':[],'len':0}

            line['words'].append(word)
            line['len'] += len(word)
        justified.append(line)
        res = []
        for line in justified:
            if line==justified[-1]:
                new_line = ' '.join(line['words'])
                new_line += ' '*(L-len(new_line))
                res.append(new_line)
                break
            words = line['words']
            words_len = line['len']
            extra_space = L - words_len
            ave_space = extra_space//(len(words)-1) if len(words)>1 else extra_space
            space_str = ' '*ave_space
            if len(words)>1:
                for i in range(extra_space%((len(words)-1))):
                    words[i] += ' '
            else:
                words[0] +=' '*extra_space

            new_line = space_str.join(words)
            res.append(new_line)

        return res


words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
L = 30
test = Solution()
res = test.fullJustify(words, L)
print(res)