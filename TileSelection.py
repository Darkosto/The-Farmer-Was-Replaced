
def is_even(n):
	return n % 2 == 0
	
def is_odd(n):
	return n % 2 != 0

def max_row():
	return get_world_size() - 1

def max_column():
	return get_world_size() - 1


#print(max_column())

def tile_selection(a = True):
	if a:
		if get_pos_y() == max_column():
			move(North)
			move(East)
		else:
			move(North)

def tile_selection_skip_column(a = True):
	if a:
		if get_pos_y() == max_column():
			move(North)
			move(East)
			move(East)
		else:
			move(North)


#if num_unlocked(Unlocks.Carrots) > 0:
#	print(num_unlocked(Unlocks.Carrots) )
#else:
#	print("No Carrots")	
	
	