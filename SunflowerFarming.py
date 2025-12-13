import TileSelection
import WaterCrops

world_size = -1
total_tiles = 0
tiles_with_petal_7 = 0
started_at_origin = 0


def only_origin_over_7():
	y = 0
	while y < world_size:
		x = 0
		while x < world_size:
			if not (x == 0 and y == 0):

				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Sunflower)
				elif get_entity_type() != Entities.Sunflower:
					plant(Entities.Sunflower)

				if get_entity_type() == Entities.Sunflower and measure() > 7:
					return False

				TileSelection.tile_selection()

			x += 1
		y += 1

	return True


def run_sunflower_farming():
	# One-time initialization
	if world_size == -1:
		world_size = get_world_size()
		total_tiles = world_size * world_size

	if started_at_origin == 0:
		if get_pos_x() == 0 and get_pos_y() == 0:
			started_at_origin = 1
			tiles_with_petal_7 = 0
		else:
			TileSelection.tile_selection()
		return False

	if started_at_origin == 1:

		if get_pos_x() == 0 and get_pos_y() == 0:
			tiles_with_petal_7 = 0

		if get_entity_type() == Entities.Sunflower:
			p = measure()

			if p != 7:
				if get_ground_type() == Grounds.Soil:
					harvest()
					plant(Entities.Sunflower)
				else:
					harvest()
					till()
					plant(Entities.Sunflower)
			else:
				tiles_with_petal_7 += 1
				quick_print(tiles_with_petal_7)

		else:
			if get_ground_type() == Grounds.Soil:
				harvest()
				plant(Entities.Sunflower)
			else:
				harvest()
				till()
				plant(Entities.Sunflower)

		TileSelection.tile_selection()

		if only_origin_over_7():
			tiles_with_petal_7 = total_tiles

		if tiles_with_petal_7 == total_tiles:
			started_at_origin = 2

		return False

	if started_at_origin == 2:
		if get_pos_x() == 0 and get_pos_y() == 0:
			if get_ground_type() == Grounds.Soil:
				if can_harvest():
					harvest()
					plant(Entities.Sunflower)
				else:
					WaterCrops.fertilize_sunflowers()
			else:
				harvest()
				till()
				plant(Entities.Sunflower)
		else:
			TileSelection.tile_selection()

		return True
