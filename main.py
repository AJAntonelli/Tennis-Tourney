import random
import json
import player

def get_tournament_bracket_data(file_path: str) -> dict:  #gets the data from the json file
    '''Get tournament bracket data from JSON file.

    Keyword arguments:
    file_path -- the file path (default None)

    '''
    f = open(file_path)
    bracket_data = json.load(f)
    f.close()
    return bracket_data

def map_players(bracket_data: dict) -> list: #associates the name and rating to players
    '''Maps JSON data to list of Player objects.

    Keywaord arguments:
    bracket_data -- Dictionary containing touranment data

    '''
    players = []
    for p in bracket_data['players']:
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
round_number = 1

bracket_data = get_tournament_bracket_data('players.json')

players = map_players(bracket_data)

#start round loop
while len(players) > 1:
    print('\nRound: ', round_number)
    
    #start match loop
    while len(players) > 1:
        player_one = players.pop()
        player_two = players.pop()
        print(player_one.name, "vs", player_two.name)
        players_next_round = player_vs_bye(players_next_round, player_one, player_two)
        win_probability(players_next_round, player_one, player_two)
    #end match loop

    #increment for next round
    round_number += 1
    players = players_next_round
    players_next_round = []
#end round loop

print('\nThe predicted winner of the tournament is: ', players[0].name)
