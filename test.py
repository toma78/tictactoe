
test = [
    'settings timebank 10000',
    'settings time_per_move 500',
    'settings player_names player1,player2',
    'settings your_bot player1',
    'settings your_botid 1',
    'update game round 1',
    'update game move 1',
    'update game field 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
    'update game macroboard -1,-1,-1,-1,-1,-1,-1,-1,-1',
    'action move 10000'
    ]

from position import Position
from randombot import RandomBot
from main import parse_command

pos = Position()
bot = RandomBot()

for t in test:
    print parse_command(t, bot, pos)    