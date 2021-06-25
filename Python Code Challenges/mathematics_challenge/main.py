class Solution:

    def run(self, number):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        isSemiprime = False

        primes = []

        while number > 1:
            for i in range(2, number + 1):
                if number % i == 0:
                    primes.append(i)
                    number = int(number /i)

        if len(primes) == 2:
            isSemiprime = True

        return isSemiprime


solution = Solution()
print(solution.run(6))