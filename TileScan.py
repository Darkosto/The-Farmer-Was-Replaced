import TileSelection
#import Crops

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
				move(d)  # move first
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
		# nothing found, work on current tile
		if get_entity_type() == Entities.Sunflower:
			TileSelection.tile_selection(1)
		else:
			till()
			plant(Entities.Sunflower)
