import random
import json

import player

##TODO move information into json bonus scrape from web

players_next_round = []
players = []
round_number = 1
def data(): #gets the data from the json file
    f = open('players.json')
    players_data = json.load(f)
    f.close()
    print(players_data)
    print(players_data['players'])
    return players,round_number,players_data

players, round_number, players_data = data()

def player_name_rating(players, players_data): #associates the name and rating to players
    for p in players_data['players']:
        players.append(player.Player(p['name'], p['rating']))

player_name_rating(players, players_data)

def win_probability(players_next_round, player_name_1, player_name_2, win_probability): #calculate win probability 
    #difference_of_ratings = abs(player_name_1.rating - player_name_2.rating)
    #if (difference_of_ratings <= 100 and difference_of_ratings >= 0):
    #    win_probability = 0.64
    #    if random.random() <= win_probability:
    #        players_next_round.append(player_name_1)
    #        print('Player One Wins!: ', player_name_1.name)
    #    else:
    #        players_next_round.append(player_name_2)
    #        print('Player Two Wins!: ', player_name_2.name)
    #if (difference_of_ratings <= 200 and difference_of_ratings > 100):
    #    win_probability = 0.76
    #    if random.random() <= win_probability:
    #        players_next_round.append(player_name_1)
    #        print('Player One Wins!: ', player_name_1.name)
    #    else:
    #        players_next_round.append(player_name_2)
    #        print('Player Two Wins!: ', player_name_2.name)  
    #if (difference_of_ratings <= 300 and difference_of_ratings > 200):
    #    win_probability = 0.85
    #    if random.random() <= win_probability:
    #    
    #        players_next_round.append(player_name_1)
    #        print('Player One Wins!: ', player_name_1.name)
    #    else:
    #        players_next_round.append(player_name_2)
    #        print('Player Two Wins!: ', player_name_2.name)   
    #if (difference_of_ratings <= 400 and difference_of_ratings > 300):
    #    win_probability = 0.91
    #    if random.random() <= win_probability:
    #    
    #        players_next_round.append(player_name_1)
    #        print('Player One Wins!: ', player_name_1.name)
    #    else:
    #        players_next_round.append(player_name_2)
    #        print('Player Two Wins!: ', player_name_2.name) 
    #if (difference_of_ratings <= 500 and difference_of_ratings > 400):
    #    win_probability = 0.95
    #    if random.random() <= win_probability:
        
    #        players_next_round.append(player_name_1)
    #        print('Player One Wins!: ', player_name_1.name)

    #    else:
    #        players_next_round.append(player_name_2)
    #       print('Player Two Wins!: ', player_name_2.name) 
    
    #if (difference_of_ratings > 500):
    #    win_probability = 0.99
    #    if random.random() <= win_probability:
    #        players_next_round(player_name_1.name)
    #        print('Player One Wins!: ', player_name_1.name)
    #    else:
    #        players_next_round(player_name_2.name)
    #        print('Player Two Wins!: ', player_name_2.name)
            

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


while len(players) > 1:
    print('\nRound: ', round_number)
    while len(players) > 1:
        player_name_1 = players.pop()
        player_name_2 = players.pop()
        print(player_name_1.name, "vs", player_name_2.name)
        player_vs_bye(players_next_round, player_name_1, player_name_2)
        win_probability(players_next_round, player_name_1, player_name_2, win_probability)
    round_number += 1
    players = players_next_round
    players_next_round = []
print('\nThe predicted winner of the tourn is: ',players[0].name)
