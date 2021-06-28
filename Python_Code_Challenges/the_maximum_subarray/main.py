class Solution:

    def run(self, a):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        maximum_sum = a[0]

        for i in range(0, len(a)):
            new_list = a[i::]
            current_sum = 0
            for number in new_list:
                current_sum += number
                if current_sum > maximum_sum:
                    maximum_sum = current_sum

        return maximum_sum


solution = Solution()
print(solution.run([-2,1,-3,4,-1,2,1,-5,4]))



