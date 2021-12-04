import random
import json
from player import Player

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

    Keyword arguments:
    bracket_data -- Dictionary containing touranment data

    '''
    players = []
    for p in bracket_data['players']:
        players.append(Player(p['name'], p['rating']))
    return players

def calculate_player_one_win_probability(player1: Player, player2: Player) -> float:
    '''Returns the win probability of the first player
    
    Keyword arguments:
    player1 -- The first player 
    player2 -- The second player
    '''
    return player1.rating / (player1.rating + player2.rating)
    
def print_winner(winner):
    '''Prints the winner of a match

    Keyword arguments:
    winner -- A Player object

    '''
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
            wp = calculate_player_one_win_probability(player_one, player_two)
            winner = player_one if random.random() <= wp else player_two
            players_next_round.append(winner)
            print_winner(winner)
    #end match loop

    #increment for next round
    round_number += 1
    players = players_next_round
    players_next_round = []
#end round loop

print('\nThe predicted winner of the tournament is:', players[0].name + '\n')
