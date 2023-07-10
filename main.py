#### ---- SETUP ---- ####

import csv
from team import Team

#### ---- LOAD TEAM DATA ---- ####

teams = []
with open("team_history.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        team = Team(line["name"], int(line["wins"]), int(line["losses"]))
        teams.append(team)

#### ---- SIMULATE SEASON ---- ####

for team in teams:
    print("Simulating " + team.name + "'s home games:\n")
    for away in teams:
        if team == away:
            continue
        team.compete(away)
    input("\nHit enter to see next match results")

#### ---- FINAL RESULTS ---- ####

print("\nFinal Results\n")
for team in teams:
    team.display_season()
