import TileSelection
import WaterCrops


def pumpkin(a = True):
	if a:
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

def carrot(a = True):
	if a:
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
				
def sunflower(a = True):
	if a:
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
					
def grass(a = True):
	if a:
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
					
def tree(a = True):
	if a:
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

def bush(a = True):
	if a:
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

def maze(a = True):
	if a:
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


def tree_only(a = True):
	if TileSelection.is_even(get_pos_x()):
		tree(1)
		grass(1)	
	else:
		grass(1)
		tree(1)		
										
def sunflower_and_tree(a = True):
	if 	random() <= 0.4:
		sunflower(1)
	if random() >= 0.41:
		tree(1)