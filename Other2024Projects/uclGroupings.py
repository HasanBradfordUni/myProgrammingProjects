def get_done_teams(file_name):
    done_teams = {}
    team_name = ""
    team_num = 0
    opponents = []
    num = 0
    with open(file_name) as file:
        if file.readline().strip().startswith("Enter team") and team_num != 0:
            done_teams[team_name] = opponents
            team_name = file.readline().strip().replace("Enter team name: ", "")
            team_num += 1
            opponents = []
            num = 0
        else:
            num += 1
            string = f"Enter opponent {num} for {team_name}: "
            opponents.append(file.readline().strip().replace(string, ""))
    return done_teams

def get_team_data(done_teams):
    teams = done_teams.copy()
    for _ in range(36-len(teams)):
        team_name = input("Enter team name: ")
        opponents = []
        for num in range(8):
            opponent = input(f"Enter opponent {num+1} for {team_name}: ")
            opponents.append(opponent)
        teams[team_name] = opponents
    return teams

def group_teams(teams):
    groups = []
    while teams:
        team, opponents = teams.popitem()
        group = {team}
        for opponent in opponents:
            if opponent in teams and team in teams[opponent]:
                group.add(opponent)
                del teams[opponent]
        groups.append(group)
    return groups

def main():
    done_teams = get_done_teams("UCL Teams, Matches, Groups.txt")
    print("Done Teams with their opponents:")
    for team, opponents in done_teams.items():
        print(f"{team}: {', '.join(opponents)}")
    teams = get_team_data(done_teams)
    groups = group_teams(teams)
    print("Groupings:")
    for i, group in enumerate(groups, 1):
        print(f"Group {i}: {', '.join(group)}")

if __name__ == "__main__":
    main()