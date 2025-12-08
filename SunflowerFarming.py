import Upgrades
import Crops
import UnlocksData
import HatActions
import TileSelection
import TileScan
import WaterCrops

world_size = get_world_size()
total_tiles = world_size * world_size
scanned_tiles = 0

# Move to origin before starting scan
while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(North)

# Main loop
while True:
	# Scan the world row by row
	for y in range(world_size):
		for x in range(world_size):
			scanned_tiles += 1

			# Handle current tile
			if get_entity_type() == Entities.Sunflower:
				p = measure()
				if p != 7:  # Only harvest if not level 7
					harvest()
					plant(Entities.Sunflower)
			else:
				if get_ground_type() == Grounds.Soil:
					harvest()
					plant(Entities.Sunflower)
				else:
					harvest()
					till()
					plant(Entities.Sunflower)

			# Move East unless at right edge
			if x < world_size - 1:
				move(East)

		# Move South to next row, return to west edge
		if y < world_size - 1:
			while get_pos_x() != 0:
				move(West)
			move(South)

	# After scanning all tiles, move to origin if all are level 7
	if scanned_tiles >= total_tiles:
		if not TileScan.at_origin:
			TileScan.sunflower_cheese()  # Moves toward origin

		if TileScan.at_origin:
			if can_harvest():
				use_item(Items.Fertilizer)
				harvest()
				plant(Entities.Sunflower)
				#WaterCrops.water_crops()
				use_item(Items.Fertilizer)
			else:
				use_item(Items.Fertilizer)

		# Reset scanned_tiles for next full scan
		scanned_tiles = 0
