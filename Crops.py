import TileSelection
import WaterCrops


def pumpkin():
	if get_entity_type() == Entities.Pumpkin:
		if can_harvest():
			harvest()
			plant(Entities.Pumpkin)
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)							
		else:
			use_item(Items.Water) 
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Soil:
			harvest()
			plant(Entities.Pumpkin)
		else:
			harvest()
			till()
			plant(Entities.Pumpkin)
			TileSelection.tile_selection(1)				

def carrot():
	if get_entity_type() == Entities.Carrot:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)							
		else:
			use_item(Items.Water) 
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Soil:
			harvest()
			plant(Entities.Carrot)
		else:
			harvest()
			till()
			plant(Entities.Carrot)
			TileSelection.tile_selection(1)			
				
def sunflower():
	if get_entity_type() == Entities.Sunflower:
		if can_harvest() and measure() > 5:
			harvest()
			plant(Entities.Sunflower)
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)
		else:
			use_item(Items.Water) 
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Soil:
			harvest()
			plant(Entities.Sunflower)
			TileSelection.tile_selection(1)
		else:
			harvest()
			till()
			plant(Entities.Sunflower)
			TileSelection.tile_selection(1)		
					
def grass():
	if get_entity_type() == Entities.Grass:
		if can_harvest():
			harvest()
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)							
		else:
			use_item(Items.Water) 
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Grassland:
			harvest()
			plant(Entities.Grass)
			TileSelection.tile_selection(1)
		else:
			harvest()
			till()
			plant(Entities.Grass)
			TileSelection.tile_selection(1)		
					
def tree():
	if get_entity_type() == Entities.Tree:
		if can_harvest():
			harvest()
			plant(Entities.Tree)
			WaterCrops.fertilize_crops()
			TileSelection.tile_selection(1)							
		else:
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Grassland:
			harvest()
			plant(Entities.Tree)
			TileSelection.tile_selection(1)	
		else:
			harvest()
			till()
			plant(Entities.Tree)						
			TileSelection.tile_selection(1)		

def bush():
	if get_entity_type() == Entities.Bush:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			#use_item(Items.Weird_Substance)
			TileSelection.tile_selection(1)							
		else:
			WaterCrops.water_crops(1)
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Grassland:
			harvest()
			plant(Entities.Bush)
		else:
			harvest()
			till()
			plant(Entities.Bush)
			TileSelection.tile_selection(1)		

def maze():
	if get_entity_type() == Entities.Bush:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			use_item(Items.Weird_Substance)
			TileSelection.tile_selection(1)							
		else:
			TileSelection.tile_selection(1)
	else:
		if get_ground_type() == Grounds.Grassland:
			harvest()
			plant(Entities.Bush)
		else:
			harvest()
			till()
			plant(Entities.Bush)
			TileSelection.tile_selection(1)		


def tree_only():
	if TileSelection.is_even(get_pos_x()):
		tree()
		grass()	
	else:
		grass()
		tree()		
										
def sunflower_and_tree():
	if 	random() <= 0.4:
		sunflower()
	if random() >= 0.41:
		tree()