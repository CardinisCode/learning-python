class Solution:

    def run(self, n, m):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        # We need to factor in the constraints:
        if len(m) == 0 or len(m) > 1000:
            return n
           
        total = n
        for i in m:
            if i % 2 == 0:
                total += i

        return total


solution = Solution()
print(solution.run(1, [5,7,8,9]))