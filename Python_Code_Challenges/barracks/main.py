import math


class Solution:

    def run(self, n, k):
        # Lets first check for the edge cases:        
        if n == 0 or k == 0:
            return 0

        if k == 1:
            return k

        # Now we can just apply the math:
        nr_ways = 0
        power = math.ceil(n/k)
        nr_ways = k ** power

        return nr_ways


solution = Solution()
print(solution.run(5, 2))