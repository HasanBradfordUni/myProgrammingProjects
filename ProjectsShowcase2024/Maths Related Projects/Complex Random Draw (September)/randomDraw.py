from random import randint, choice

def random_draw(teams, matches, opponents, sameCountry, samePot, eachCountryMax, eachPot, homeGames, awayGames):
	pot1Teams = []
	pot2Teams = []
	pot3Teams = []
	pot4Teams = []
	teamCountries = {}
	prevMatches = []
	for num in range(0, len(teams)):
		teamsDict = teams[num]
		if num == 0:
			pot1Teams.extend(teamsDict)
			print("Pot 1 teams are:",pot1Teams)
		elif num == 1:
			pot2Teams.extend(teamsDict)
			print("Pot 2 teams are:",pot2Teams)
		elif num == 2:
			pot3Teams.extend(teamsDict)
			print("Pot 3 teams are:",pot3Teams)
		else:
			pot4Teams.extend(teamsDict)
			print("Pot 4 teams are:",pot4Teams)
		for team in teamsDict.items():
			teamCountries[team[0]] = team[1]
	for team in pot1Teams:
		gamesAtHome = 0
		gamesAway = 0
		while gamesAtHome < homeGames:
			homeTeam = team
			homeTeamCountry = teamCountries[team]
			for num in range(samePot//2):
				awayTeamCountry = homeTeamCountry
				while awayTeamCountry == homeTeamCountry:
					awayTeam = choice(pot1Teams)
					awayTeamCountry = teamCountries[awayTeam]
				prevMatches.append((homeTeam, awayTeam))
				gamesAtHome += (homeGames/samePot)*2
		while gamesAway < awayGames:
			awayTeam = team
			awayTeamCountry = teamCountries[team]
			for num in range(samePot//2):
				homeTeamCountry = awayTeamCountry
				while homeTeamCountry == awayTeamCountry:
					homeTeam = choice(pot1Teams)
					homeTeamCountry = teamCountries[homeTeam]
				prevMatches.append((homeTeam, awayTeam))
				gamesAway += (awayGames/samePot)*2
	index = -1
	for num in range(len(prevMatches)):
		if (num % 2 == 0):
			index += 1
			print(f'Matches for {pot1Teams[index]}\n')
			
		match = prevMatches[num]
		print(match[0],"Vs",match[1])
		print(match[0],"is at Home and",match[1],"is Away\n")
			
	
			
teams = [{"Real Madrid": "Spain", "Man City": "England", "Bayern": "Germany", "Paris SG": "France", "Inter": "Italy", "Liverpool": "England", "Dortmund": "Germany", "Leipzig": "Germany", "Barca": "Spain"},
{"Atletico Madrid": "Spain", "Arsenal": "England", "Leverkusen": "Germany", "Atalanta": "Italy", "Juve": "Italy", "Benfica": "Portugal", "Ac Milan": "Italy", "Club Brugge": "Belgium", "Shaktar": "Ukraine"},
{"Feyenoord": "Netherlands", "Sporting": "Portugal", "PSV": "Netherlands", "Lille": "France", "Dinamo": "Croatia", "Salzburg": "Austria", "Crevena": "Czechia", "Young Boys": "Switzerland", "Celtic": "Scotland"},
{"Girona": "Spain", "Aston Villa": "England", "Stuttgart": "Germany", "Monaco": "France", "Bologna": "Italy", "Slovan": "Slovakia", "Sparta": "Czechia", "Brest": "France", "Sturm": "Austria"}]
matches = 8
opponents = 8
sameCountry = 0
samePot = 2
eachCountryMax = 2
eachPot = 2
homeGames = 4
awayGames = 4
random_draw(teams, matches, opponents, sameCountry, samePot, eachCountryMax, eachPot, homeGames, awayGames)