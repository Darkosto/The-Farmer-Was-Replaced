import TileSelection
import WaterCrops

def run_sunflower_farming():
	world_size = get_world_size()
	total_tiles = world_size * world_size
	tiles_with_petal_7 = 0
	started_at_origin = 0

	def only_origin_over_7():
		for y in range(world_size):
			for x in range(world_size):
				if x == 0 and y == 0:
					continue  # skip origin
				TileSelection.tile_selection()  # move to next tile
				if get_entity_type() == Entities.Sunflower and measure() > 7:
					return False
		return True

	while True:
		if started_at_origin == 0:
			if get_pos_x() == 0 and get_pos_y() == 0:
				started_at_origin = 1
				tiles_with_petal_7 = 0
			else:
				TileSelection.tile_selection()
			continue

		if started_at_origin == 1:

			if get_pos_x() == 0 and get_pos_y() == 0:
				tiles_with_petal_7 = 0

			# Check current tile
			if get_entity_type() == Entities.Sunflower:
				p = measure()
				if p != 7:
					if get_ground_type() == Grounds.Soil:
						harvest()
						plant(Entities.Sunflower)
						TileSelection.tile_selection()
					else:
						harvest()
						till()
						plant(Entities.Sunflower)
						TileSelection.tile_selection()
				else:
					tiles_with_petal_7 += 1
					quick_print(tiles_with_petal_7)
					TileSelection.tile_selection()
			else:
				if get_ground_type() == Grounds.Soil:
					harvest()
					plant(Entities.Sunflower)
				else:
					harvest()
					till()
					plant(Entities.Sunflower)

			if only_origin_over_7():
				tiles_with_petal_7 = total_tiles

			if tiles_with_petal_7 == total_tiles:
				started_at_origin = 2
			continue

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
