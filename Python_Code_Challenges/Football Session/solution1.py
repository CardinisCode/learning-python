import json
import urllib.request


class Solution:
    def __init__(self, data):
        self.data = data

    def run(self, teamKey):
        goals = 0
        for round_items in self.data["rounds"]:
            for match_items in round_items["matches"]:
                for team, info in match_items.items():
                    if team == "date":
                        continue
                    if team == "team1" and info["key"] == teamKey:
                        goals += match_items["score1"]
                    elif team == "team2" and info["key"] == teamKey:
                        goals += match_items["score2"]

        return goals


resource_file = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json"
request = urllib.request.urlopen(resource_file)
data = json.load(request)

solution = Solution(data)
print(solution.run("liverpool"))
