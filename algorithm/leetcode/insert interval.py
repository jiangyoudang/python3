# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        # if not intervals:
        #     return [newInterval]
        start_interval = 0
        end_interval = len(intervals)
        start = newInterval.start
        end = newInterval.end


        for i in range(len(intervals)):
            if intervals[i].start <= newInterval.start <= intervals[i].end:
                start_interval = i
                start = intervals[i].start
            elif intervals[i].end <newInterval.start:
                start_interval = i+1
                start = newInterval.start
            if intervals[i].start <= newInterval.end <= intervals[i].end:
                end_interval = i+1
                end = intervals[i].end
                break
            elif newInterval.end < intervals[i].start:
                end_interval = i
                end = newInterval.end
                break

        intervals[start_interval:end_interval] = [Interval(start, end)]

        return intervals


test = Solution()

intervals = [Interval(1,5), Interval(6, 8)]
res = test.insert(intervals, Interval(5,6))