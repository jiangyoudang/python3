import collections
class Solution:
    # @return a string
    def minWindow(self, S, T):
        need_T = {}
        count = 0
        queue = collections.deque()
        T_len = len(T)
        S_len = len(S)
        window = (0, S_len)

        for i in T:
            need_T[i] = need_T.setdefault(i,0) + 1

        for i in range(len(S)):
            if S[i] not in need_T:
                continue
            else:
                need_T[S[i]] -= 1
                if need_T[S[i]] >= 0:
                    count += 1
                queue.append((S[i],i))

                while count == T_len:
                    tmp = (queue[0][1], queue[-1][1])
                    if tmp[1]-tmp[0] < window[1] - window[0]:
                        window = tmp

                    if need_T[queue[0][0]]<0:
                        p = queue.popleft()
                        need_T[p[0]] += 1
                    else:
                        break

        if window[1] == S_len:
            return ''
        else:
            return S[window[0]:window[1]+1]


test = Solution()
res = test.minWindow('ADOBECODEBANC','ABC')
print(res)