import random
import json

import player

##TODO move information into json bonus scrape from web

#players = players[:36] #TODO get the actual players into the correct matches
players_next_round = []
players = []
round_number = 1
f = open('players.json')
players_data = json.load(f)
f.close()
print(players_data)
print(players_data['players'])
for p in players_data['players']:
    players.append(player.Player(p['name'], p['rating']))

while len(players) > 1:
    print('\nRound: ', round_number)
    while len(players) > 1:
        player_name_1 = players.pop()
        player_name_2 = players.pop()
        if player_name_1.name == "BYE" or player_name_2.name == "BYE":
            if player_name_1.name == "BYE":
                players_next_round.append(player_name_2)
            else:
                players_next_round.append(player_name_1)
        ##calculate how likely the player is to win
        #TODO get a more accurate probability for each player to win
        win_probability = player_name_1.rating / (player_name_1.rating + player_name_2.rating)
        #randomize outcome
        if random.random() <= win_probability:
            players_next_round.append(player_name_1)
            print('Player One Wins!: ',player_name_1.name)
        else:
            players_next_round.append(player_name_2)
            print('Player Two Wins!: ', player_name_2.name)
    round_number += 1
    players = players_next_round
    players_next_round = []
print('\nThe predicted winner of the tourn is: ',players[0].name)
