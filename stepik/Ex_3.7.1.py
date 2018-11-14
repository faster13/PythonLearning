games_num = int(input())
#sample_teams = ["ЦСКА;0;Зенит;2", "Спартак;1;ЦСКА;1", "Зенит;3;Спартак;1"]
teams = {}
while games_num != 0:
    masInp = str(input()).split(";")
    #masInp = sample_teams[games_num - 1].split(";")
    #Команда:Всего_игр Побед Ничьих Поражений Всего_очков
    dataTeamA = [1, 0, 0, 0, 0]
    dataTeamB = [1, 0, 0, 0, 0]
    if(int(masInp[1]) == int(masInp[3])):
        dataTeamA[2] = 1
        dataTeamB[2] = 1
        dataTeamA[4] = 1
        dataTeamB[4] = 1
    if(int(masInp[1]) > int(masInp[3])):
        dataTeamA[1] = 1
        dataTeamA[4] = 3
        dataTeamB[3] = 1
    if(int(masInp[1]) < int(masInp[3])):
        dataTeamB[1] = 1
        dataTeamB[4] = 3
        dataTeamA[3] = 1
    if masInp[0] not in teams.keys():
        teams[masInp[0]] = dataTeamA
    elif masInp[0] in teams.keys():
        teams[masInp[0]] = [oldData + newData for oldData, newData in zip(teams[masInp[0]], dataTeamA)]
    if masInp[2] not in teams.keys():
        teams[masInp[2]] = dataTeamB
    elif masInp[2] in teams.keys():
        teams[masInp[2]] = [oldData + newData for oldData, newData in zip(teams[masInp[2]], dataTeamB)]
    games_num -= 1
for team_name, score in teams.items():
    print(team_name + ": ", end = "")
    [print(str(point) + " ", end = " ") for point in score]
    print()