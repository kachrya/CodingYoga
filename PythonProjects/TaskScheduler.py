import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

        However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

        You need to return the least number of intervals the CPU will take to finish all the given tasks.

        Example 1:
        Input: tasks = ['A','A','A','B','B','B'], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
        Note:
        The number of tasks is in the range [1, 10000].
        The integer n is in the range [0, 100].
        E C A B
        E C A B
        E C A _
        E C _ _
        E C _ _
        E C
        """

        c = collections.Counter(tasks)
        print(c)
        for max_task, max_count in c.most_common(1):
            idle_cycles = (max_count-1) * n
        total_cycles = idle_cycles + max_count
        print(total_cycles, idle_cycles)

        for x, count in c.most_common():
            if x is max_task:
                continue
            if idle_cycles > 0:
                if count == max_count:
                    total_cycles += 1
                    idle_cycles -= (count -1)
                    continue
                else:
                    # count < max_count
                    idle_cycles -= count
            elif idle_cycles < 0:
                idle_cycles == 0
                total_cycles += (-idle_cycles)
            else:
                total_cycles = total_cycles + count

        return total_cycles



soln = Solution()
#cycles = soln.leastInterval(['A','A','A','B','B', 'C', 'C', 'C', 'C', 'C', 'C', 'E','E','E','E','E', 'E'], 1)
cycles = soln.leastInterval(['A','A','A','B','B','B'], 0)
print(cycles)