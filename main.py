import random


##TODO move information into json bonus scrape from web
players = ['CG', 'TP', 'FT', 'UH', 'DJ', 'GM', 'RO',
"CM", "LS", "CA", "JI", 'CN', 'AK', 'MC', 
'GD', 'RBA', 'AB', 'MG', 'HH', 'ADF', 'SK',
'LD', 'BN', 'MM', 'KA', 'KK', 'RG', 'AM', 
'FK', 'ADM', 'DE', 'DS', 'YN', 'LH', 'MF',
'FAA', 'HFT', 'ARV', 'DK', 'JLS', 'FF', 'NB',
'JS', 'FD', 'DG', 'GP', 'MK', 'BP',
'ST', 'AZ', 'DM', 'PCB','AR','DS', 'CR',
'MB']
players = players[:36] #TODO get the actual players into the correct matches
players_next_round = []
round_number = 1
while len(players) > 1:
    print('\nRound: ', round_number)
    while len(players) > 1:
        player_name_1 = players.pop()
        player_name_2 = players.pop()
        ##calculate how likely the player is to win
        #TODO get a more accurate probability for each player to win
        win_probability = 0.5
        #randomize outcome
        if random.random() <= win_probability:
            players_next_round.append(player_name_1)
            print('Player One Wins!: ',player_name_1)
        else:
            players_next_round.append(player_name_2)
            print('Player Two Wins!: ', player_name_2)
    round_number += 1
    players = players_next_round
    players_next_round = []
print('\nThe predicted winner of the tourn is: ',players[0])