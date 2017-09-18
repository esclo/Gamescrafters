from solve import *

init_pos = 4

def generate_moves(pos):
	if pos == 0:
		return []
	elif pos == 1:
		return [1]
	else:
		return [1, 2]


def do_move(pos, act):
	return pos - act


def primitive(pos):
	return 0 if not pos else 2


print(solve(init_pos, primitive, generate_moves, do_move))
