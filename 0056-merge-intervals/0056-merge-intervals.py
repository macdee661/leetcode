class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        new_intervals = [intervals[0]]
        index = 0
        for  interval in intervals:
            if interval[0] <= new_intervals[index][1]:
                new_intervals[index] = [min(interval[0], new_intervals[index][0]), max(interval[1], new_intervals[index][1])]
            else:
                index += 1
                new_intervals.append(interval)
        return new_intervals