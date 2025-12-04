import Crops
import TileSelection
import Upgrades
import Mazes
import TileScan
import HatActions



while True:

	hat_already_worn = False 

	if (
		Upgrades.maze_unlocked()
		and num_items(Items.Gold) < 5000
	):
		Crops.maze(1)
		if not hat_already_worn:
			HatActions.wear_hat(5)
			hat_already_worn = True

	elif (
		Upgrades.sunflower_unlocked()
		and num_items(Items.Power) > 4900
		and num_items(Items.Power) < 5000
	):
		Crops.sunflower_and_tree(1)
		if not hat_already_worn:
			HatActions.wear_hat(12)
			hat_already_worn = True		

	elif (
		Upgrades.pumpkin_unlocked()
		and Upgrades.pumpkin_cost() > num_items(Items.Carrot)
		and Upgrades.carrot_plant_cost() * 20 > num_items(Items.Hay)
	):
		Crops.carrot(1)
		if Upgrades.pumpkin_cost() < num_items(Items.Carrot):
			print("Unlocking Pumpkin Upgrade")
			unlock(Unlocks.Pumpkins)
		if not hat_already_worn:
			HatActions.wear_hat(3)
			hat_already_worn = True			

	elif (
		Upgrades.tree_unlocked() 
		and Upgrades.tree_cost() > num_items(Items.Hay)
	):	
		Crops.grass(1)
		if Upgrades.tree_cost() < num_items(Items.Hay):
			print("Unlocking Tree Upgrade")
			unlock(Unlocks.Trees)
		if not hat_already_worn:
			HatActions.wear_hat(11)
			hat_already_worn = True

	elif (
		Upgrades.carrot_unlocked() 
		and Upgrades.carrot_cost() > num_items(Items.Wood)
	):
		Crops.tree_only(1)	
		if Upgrades.carrot_cost() < num_items(Items.Wood):
			print("Unlocking Carrot Upgrade")
			unlock(Unlocks.Carrots)
		if not hat_already_worn:
			HatActions.wear_hat(11)
			hat_already_worn = True					

	elif (
		Upgrades.grass_cost() > num_items(Items.Wood)
	):
		Crops.tree_only(1)
		if Upgrades.grass_cost() < num_items(Items.Wood):
			print("Unlocking Grass Upgrade")
			unlock(Unlocks.Grass)

	else:		
		#TileSelection.tile_selection(1)		

		if TileSelection.is_even(get_pos_x()):
	
			if get_pos_y() in {0, 8, 12, 14}:
				Crops.tree(1)
			if get_pos_y() in {1, 9, 11, 15, 16}:
				Crops.grass(1)
			if get_pos_y() in {2, 3, 10, 13}:
				Crops.carrot(1)
			if get_pos_y() == 4:
				Crops.sunflower(1)
			if get_pos_y() in {5, 6, 7, 28, 29, 30, 31}:
				Crops.pumpkin(1)				
	
		if TileSelection.is_odd(get_pos_x()):
			if get_pos_y() in {0, 8, 11, 14, 16}:
				Crops.grass(1)
			if get_pos_y() in {1, 4}:
				Crops.sunflower(1)	
			if get_pos_y() in {2, 9, 10, 12, 13}:
				Crops.carrot(1)
			if get_pos_y() in {3, 8, 13, 15}:
				Crops.tree(1)			
			if get_pos_y() in {5, 6, 7, 28, 29, 30, 31}:
				Crops.pumpkin(1)