import Crops
import TileSelection
import Upgrades
import HatActions
import SunflowerFarming

while True:
	# Flags
	hat_already_worn = False

	if not num_items(Items.Power) < 5000:
		power_level = False
	if num_items(Items.Power) > 50000:
		power_level = True

	# Maze priority
	if Upgrades.maze_unlocked() and num_items(Items.Gold) < 5000:
		Crops.maze()
		if not hat_already_worn:
			HatActions.wear_hat(5)
			hat_already_worn = True

	# Sunflower priority
	elif (Upgrades.sunflower_unlocked() and
		num_items(Items.Fertilizer) > 1000 and
		not power_level):
		done = SunflowerFarming.run_sunflower_farming()
		if not hat_already_worn:
			HatActions.wear_hat(12)
			hat_already_worn = True



	# Lowest upgrade
	else:
		if Upgrades.lowest_upgrade == "GrassLevel":
			Crops.tree_only()
			Upgrades.grass_upgrade()
			if not hat_already_worn:
				HatActions.wear_hat(10)
				hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "PumpkinLevel" and
			  Upgrades.pumpkin_unlocked() and
			  Upgrades.pumpkin_cost() > num_items(Items.Carrot) and
			  Upgrades.carrot_plant_cost() * 20 < num_items(Items.Hay)):
			Crops.carrot()
			Upgrades.pumpkin_upgrade()
			if not hat_already_worn:
				HatActions.wear_hat(3)
				hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "CarrotLevel" and
			  Upgrades.pumpkin_unlocked() and
			  Upgrades.pumpkin_cost() > num_items(Items.Carrot) and
			  Upgrades.carrot_plant_cost() * 20 > num_items(Items.Hay)):
			Crops.tree_only()
			Upgrades.carrot_upgrade()
			if not hat_already_worn:
				HatActions.wear_hat(11)
				hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "TreeLevel" and
			  Upgrades.grass_cost() > num_items(Items.Wood) and
			  Upgrades.tree_unlocked() and
			  Upgrades.tree_cost() > num_items(Items.Hay)):
			Crops.grass()
			Upgrades.tree_upgrade()
			if not hat_already_worn:
				HatActions.wear_hat(11)
				hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "CactusLevel" and
			  Upgrades.pumpkin_cost() > num_items(Items.Pumpkin) and
			  Upgrades.pumpkin_unlocked()):
			Crops.pumpkin()
			Upgrades.cactus_upgrade()
			#if not hat_already_worn and Upgrades.cactus_unlocked():
			#	HatActions.wear_hat(2)
			#	hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "FertilizerLevel" and
			  Upgrades.fertilizer_cost() > num_items(Items.Wood) and
			  Upgrades.fertilizer_unlocked()):
			Crops.sunflower_and_tree()
			Upgrades.fertilizer_upgrade()
			if not hat_already_worn:
				HatActions.wear_hat(11)
				hat_already_worn = True

		elif (Upgrades.lowest_upgrade == "FertilizerLevel" and
			  Upgrades.fertilizer_cost() < num_items(Items.Wood)):
			Upgrades.fertilizer_upgrade()



		else:
			if TileSelection.is_even(get_pos_x()):
				if get_pos_y() in {0, 8, 12, 14}:
					Crops.tree()
				if get_pos_y() in {1, 9, 11, 15, 16}:
					Crops.grass()
				if get_pos_y() in {2, 3, 10, 13}:
					Crops.carrot()
				if get_pos_y() == 4:
					Crops.sunflower()
				if get_pos_y() in {5, 6, 7, 28, 29, 30, 31}:
					Crops.pumpkin()

			elif TileSelection.is_odd(get_pos_x()):
				if get_pos_y() in {0, 8, 11, 14, 16}:
					Crops.grass()
				if get_pos_y() in {1, 4}:
					Crops.sunflower()
				if get_pos_y() in {2, 9, 10, 12, 13}:
					Crops.carrot()
				if get_pos_y() in {3, 8, 13, 15}:
					Crops.tree()
				if get_pos_y() in {5, 6, 7, 28, 29, 30, 31}:
					Crops.pumpkin()
