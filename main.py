import Crops
import TileSelection
import Upgrades
import Mazes
import TileScan
import HatActions

hat_already_worn = False 

while True:

	if (
		Upgrades.maze_unlocked()
		and num_items(Items.Gold) < 5000
	):
		Crops.maze()
		if not hat_already_worn:
			HatActions.wear_hat(5)
			hat_already_worn = True

	elif (
		Upgrades.sunflower_unlocked()
		and num_items(Items.Power) > 4900
		and num_items(Items.Power) < 5000
	):
		Crops.sunflower_and_tree()
		if not hat_already_worn:
			HatActions.wear_hat(12)
			hat_already_worn = True		

	elif (
		Upgrades.pumpkin_unlocked()
		and Upgrades.pumpkin_cost() > num_items(Items.Carrot)
		and Upgrades.carrot_plant_cost() * 20 > num_items(Items.Hay)
	):
		Crops.carrot()
		if Upgrades.pumpkin_cost() < num_items(Items.Carrot):
			print("Unlocking Pumpkin Upgrade")
			unlock(Unlocks.Pumpkins)
		if not hat_already_worn:
			HatActions.wear_hat(3)
			hat_already_worn = True
		if HatActions.wear_hat(3):
			print("Hat Already On!")

	elif (
		Upgrades.tree_unlocked() 
		and Upgrades.tree_cost() > num_items(Items.Hay)
	):	
		Crops.grass()
		if Upgrades.tree_cost() < num_items(Items.Hay):
			print("Unlocking Tree Upgrade")
			unlock(Unlocks.Trees)
		if not hat_already_worn:
			HatActions.wear_hat(11)
			hat_already_worn = True
		if HatActions.hat_type_worn == 11:
			#print("Hat Already On!")
			pass	

	elif (
		Upgrades.carrot_unlocked() 
		and Upgrades.carrot_cost() > num_items(Items.Wood)
	):
		Crops.tree_only()	
		if Upgrades.carrot_cost() < num_items(Items.Wood):
			print("Unlocking Carrot Upgrade")
			unlock(Unlocks.Carrots)
		if not hat_already_worn:
			HatActions.wear_hat(11)
			hat_already_worn = True					

	elif (
		Upgrades.grass_cost() > num_items(Items.Wood)
	):
		Crops.tree_only()
		if Upgrades.grass_cost() < num_items(Items.Wood):
			print("Unlocking Grass Upgrade")
			unlock(Unlocks.Grass)

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
	
		if TileSelection.is_odd(get_pos_x()):
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