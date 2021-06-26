from collections import Counter


class Solution:

    def run(self, student_list):
        single_student_number = None
        if len(student_list) == 1:
            single_student_number = student_list[0]

        team_count = Counter(student_list)
        for team, count in team_count.items():
            if count == 1:
                single_student_number = team

        return single_student_number


solution = Solution()
print(solution.run([1, 2, 1]))