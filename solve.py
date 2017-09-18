def solve(init_pos, primitive, generate_moves, do_move):
	if primitive(init_pos) == 0:
		return 0
	else:
		next_pos = [do_move(init_pos, move) for move in generate_moves(init_pos)]
		return 1-min([solve(pos, primitive, generate_moves, do_move) for pos in next_pos])
