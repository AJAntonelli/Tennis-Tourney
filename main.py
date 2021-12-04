import random
import json
import player

def data(): #gets the data from the json file
    f = open('players.json')
    players_data = json.load(f)
    f.close()
    print(players_data)
    print(players_data['players'])
    return players_data

def player_name_rating(players, players_data): #associates the name and rating to players
    for p in players_data['players']:
        players.append(player.Player(p['name'], p['rating']))
    return players

#calculate win probability 
def win_probability(players_next_round, player_name_1, player_name_2):
    win_probability = player_name_1.rating / (player_name_1.rating + player_name_2.rating)
    if random.random() <= win_probability:
        
        players_next_round.append(player_name_1)
        print('Player One Wins!: ',player_name_1.name)
    else:
        players_next_round.append(player_name_2)
        print('Player Two Wins!: ', player_name_2.name)
        
def player_vs_bye(players_next_round, player_name_1, player_name_2): #what if a player goes against a bye
    if player_name_1.name == "BYE" or player_name_2.name == "BYE":
        if player_name_1.name == "BYE":
            players_next_round.append(player_name_2)
        else:
            players_next_round.append(player_name_1)
    return players_next_round

#Program Start
players_next_round = []
players = []
round_number = 1

players_data = data()

players = player_name_rating(players, players_data)

while len(players) > 1:
    print('\nRound: ', round_number)
    while len(players) > 1:
        player_name_1 = players.pop()
        player_name_2 = players.pop()
        print(player_name_1.name, "vs", player_name_2.name)
        players_next_round = player_vs_bye(players_next_round, player_name_1, player_name_2)
        win_probability(players_next_round, player_name_1, player_name_2)
    round_number += 1
    players = players_next_round
    players_next_round = []
print('\nThe predicted winner of the tournament is: ', players[0].name)
