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

def calculate_win_probability(player1, player2):
    return player1.rating / (player1.rating + player2.rating)
    
def determine_winner(player1, player2, win_probability):   
    if random.random() <= win_probability:
        players_next_round.append(player1)
        return player1
    else:
        players_next_round.append(player2)
        return player2

def print_winner(winner):
    print(winner.name, 'wins!')

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
        print("\n" + player_one.name, "vs", player_two.name)

        #check for bye, determine winner, append winner to next round
        if player_one.is_bye() or player_two.is_bye():
            if player_one.is_bye():
                players_next_round.append(player_two)
            else:
                players_next_round.append(player_one)
        else:
            wp = calculate_win_probability(player_one, player_two)
            winner = determine_winner(player_one, player_two, wp)
            print_winner(winner)
    #end match loop

    #increment for next round
    round_number += 1
    players = players_next_round
    players_next_round = []
#end round loop

print('\nThe predicted winner of the tournament is:', players[0].name + '\n')
