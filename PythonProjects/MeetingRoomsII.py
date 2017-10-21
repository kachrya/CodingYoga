from operator import itemgetter
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

        For example,
        Given [[0, 30],[5, 10],[15, 20]],
        return 2.
        :type intervals: List[Interval]
        :rtype: int
        """

        if intervals == []:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start, reverse=False)
        for i in intervals:
            print(i.start, i.end)
        end = 0
        rooms = 1
        for i in intervals:
            start = i.start
            if start < end:
                rooms += 1
            if end != 0:
                end = min(i.end, end)
            else:
                end = i.end

        print(rooms)
        return rooms


soln = Solution()
interval1 = Interval()
interval1.start = 1
interval1.end = 3
interval2 = Interval()
interval2.start = 4
interval2.end = 9
interval3 = Interval()
interval3.start = 4
interval3.end = 9

soln.minMeetingRooms([interval1, interval2, interval3])
#soln.minMeetingRooms([[5, 10],[0, 30],[15, 20]])
# soln.minMeetingRooms([])