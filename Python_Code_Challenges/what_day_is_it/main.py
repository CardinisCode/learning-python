from datetime import datetime, timedelta
import calendar


class Solution:

    def run(self, birthday_date):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        
        bday, bmonth = birthday_date.split("-")
        start_year = 2016
        birthday_date += "-" + str(start_year)
        end_date = "12-12-" + str(int(start_year + 49))
        start_date = datetime.strptime(birthday_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

        delta = end_date - start_date
        weekend_days = ['Fri', 'Sat', 'Sun']
        dates_list = []

        dd = [start_date + timedelta(days=x) for x in range(0, (delta).days + 1)]
        for i in dd:
            day_of_week = calendar.day_abbr[i.weekday()]
            if i.day == int(bday) and i.month == int(bmonth) and day_of_week in weekend_days:
                dates_list.append(day_of_week + "-" + str(i.year))

        return " ".join(dates_list)

solution = Solution()
print(solution.run("23-10"))