#craps-game.py
""" Simulating the dice game craps """
import random

#initialize a gamestatus variable
game_status = None
def roll_dice():
    """ Roll 2 dice and return their value as tuple"""
    die_1 = random.randrange(1,7)
    die_2 = random.randrange(1,7)
    return (die_1,die_2)

def display_dice(dice):
    """Display one roll of 2 dice"""
    die_1,die_2 = dice
    print(f'Player rolled {die_1}+{die_2} = {sum(dice)}')

dice_value = roll_dice()
display_dice(dice_value)
sum_values = sum(dice_value)

# if the sum is 7 or 11 in the first roll the player wins.
if sum_values in ( 7,11):
    game_status = 'WON'
elif sum_values in (2,3,12):
    game_status = 'LOST'
else:
    game_status = 'CONTINUE'

# Store the result to first rolls
my_point = sum_values

#Keep rolling the dice till the sum equals the sum of first roll or 7 ( in which case the player lose)
while game_status == 'CONTINUE':
    dice_value = roll_dice()
    display_dice(dice_value)
    sum_values = sum(dice_value)
    if sum_values == my_point:
        game_status = 'WON'
    if sum_values == 7:
        game_status = 'LOST'


print (f'The Player {game_status}')
