import TileSelection

def sunflower_tilescan():
	directions = [North, South, East, West]
	priorities = [15, 14, 13, 12, 11, 10]

	moved = False

	i = 0
	while i < len(priorities):
		target = priorities[i]
		j = 0
		while j < len(directions):
			d = directions[j]
			if measure(d) == target:
				move(d)
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
				moved = True
				break
			j = j + 1
		if moved:
			break
		i = i + 1

	if not moved:
		if get_entity_type() == Entities.Sunflower:
			TileSelection.tile_selection(1)
		else:
			till()
			plant(Entities.Sunflower)

# Sunflower Cheese
at_origin = False
def sunflower_cheese():
	global at_origin 
	if get_pos_x() != 0:
		move(West)
	if get_pos_y() != 0:
		move(South)
	if get_pos_x() == 0 and get_pos_y() == 0:
		at_origin = True

def move_to_tile(target_x, target_y):
	while get_pos_x() != target_x:
		if get_pos_x() < target_x:
			move(East)
		else:
			move(West)
	while get_pos_y() != target_y:
		if get_pos_y() < target_y:
			move(South)
		else:
			move(North)

def grid_list():
	world_size = get_world_size()
	all_coords = []
	for y in range(world_size):
		for x in range(world_size):
			all_coords.append((x, y))
	return all_coords

tiles_scanned = []

def record_current_tile():
	global tiles_scanned
	x = get_pos_x()
	y = get_pos_y()
	if (x, y) not in tiles_scanned:
		tiles_scanned.append((x, y))
	return tiles_scanned

def scan_full_grid():
	world_size = get_world_size()
	total_tiles = world_size * world_size
	record_current_tile()
	TileSelection.tile_selection(1)
	# Check if scanning is complete
	if len(tiles_scanned) == total_tiles:
		print("FULL GRID SCANNED!")
		at_origin = False      # reset
		return True
	return False
	
##### Usage
#while scan_full_grid() == False:
#	scan_full_grid()