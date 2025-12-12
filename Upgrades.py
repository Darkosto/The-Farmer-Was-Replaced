def pumpkin_unlocked():
	return num_unlocked(Unlocks.Pumpkins) > 0

def carrot_unlocked():
	return num_unlocked(Unlocks.Carrots) > 0	

def tree_unlocked():
	return num_unlocked(Unlocks.Trees) > 0

def maze_unlocked():
	return num_unlocked(Unlocks.Mazes) > 0

def sunflower_unlocked():
	return num_unlocked(Unlocks.Sunflowers) > 0

def speed_unlocked():
	return num_unlocked(Unlocks.Speed) > 0

def fertilizer_unlocked():
	return num_unlocked(Unlocks.Fertilizer) > 0

def watering_unlocked():
	return num_unlocked(Unlocks.Watering) > 0

def cactus_unlocked():
	return num_unlocked(Unlocks.Cactus) > 0

#############################################

def grass_level():
	return num_unlocked(Unlocks.Grass)

def pumpkin_level():
	return num_unlocked(Unlocks.Pumpkins)

def carrot_level():
	return num_unlocked(Unlocks.Carrots)

def tree_level():
	return num_unlocked(Unlocks.Trees)

def maze_level():
	return num_unlocked(Unlocks.Mazes)

def speed_level():
	return num_unlocked(Unlocks.Speed)

def fertilizer_level():
	return num_unlocked(Unlocks.Fertilizer)

def watering_level():
	return num_unlocked(Unlocks.Watering)

def cactus_level():
	return num_unlocked(Unlocks.Cactus)

#############################################

# Grass Upgrade Requires Wood
def grass_cost():
	cost_dict = get_cost(Unlocks.Grass, grass_level())
	for item in cost_dict:
		return cost_dict[item]

# Pumpkin Upgrade Requires Carrots
def pumpkin_cost():
	cost_dict = get_cost(Unlocks.Pumpkins, pumpkin_level())
	for item in cost_dict:
		return cost_dict[item]

# Carrot Upgrade Requires Wood
def carrot_cost():
	cost_dict = get_cost(Unlocks.Carrots, carrot_level())
	for item in cost_dict:
		return cost_dict[item]

# Tree Upgrade Requires Hay
def tree_cost():
	cost_dict = get_cost(Unlocks.Trees, tree_level())
	for item in cost_dict:
		return cost_dict[item]	
	
# Speed Upgrade Requires Hay, Wood, or Carrots
def speed_cost():
	cost_dict = get_cost(Unlocks.Speed, speed_level())
	for item in cost_dict:
		return cost_dict[item]	
	
# Fertilizer Upgrade Requires Wood	
def fertilizer_cost():
	cost_dict = get_cost(Unlocks.Fertilizer, fertilizer_level())
	for item in cost_dict:
		return cost_dict[item]	

# Watering Upgrade Requires Wood	
def watering_cost():
	cost_dict = get_cost(Unlocks.Watering, watering_level())
	for item in cost_dict:
		return cost_dict[item]

# Cactus Upgrade Requires Pumpkin	
def cactus_cost():
	cost_dict = get_cost(Unlocks.Cactus, cactus_level())
	for item in cost_dict:
		return cost_dict[item]	
	
#############################################

# Planting Carrots
def carrot_plant_cost():
	cost_dict = get_cost(Entities.Carrot)
	for item in cost_dict:
		return cost_dict[item]

#############################################
### Upgrade Priority System

available_upgrade_list = {
	"GrassLevel": grass_level(), 
	"PumpkinLevel": pumpkin_level(), 
	"CarrotLevel": carrot_level(),
	"TreeLevel": tree_level(),
	"SpeedLevel": speed_level(),
	"FertilizerLevel": fertilizer_level(),
	"WateringLevel": watering_level(),
	"CactusLevel": cactus_level()	
}

def upgrade_maxxed(upgrade_name):
	if upgrade_name == "GrassLevel":
		return get_cost(Unlocks.Grass) == {}
	elif upgrade_name == "PumpkinLevel":
		return get_cost(Unlocks.Pumpkins) == {}
	elif upgrade_name == "CarrotLevel":
		return get_cost(Unlocks.Carrots) == {}
	elif upgrade_name == "TreeLevel":
		return get_cost(Unlocks.Trees) == {}
	elif upgrade_name == "SpeedLevel":
		return get_cost(Unlocks.Speed) == {}
	elif upgrade_name == "FertilizerLevel":
		return get_cost(Unlocks.Fertilizer) == {}
	elif upgrade_name == "WateringLevel":
		return get_cost(Unlocks.Watering) == {}
	elif upgrade_name == "CactusLevel":
		return get_cost(Unlocks.Cactus) == {}		
	else:
		return True

lowest_value = None
lowest_upgrade = None
for key in available_upgrade_list:
	if not upgrade_maxxed(key):
		level = available_upgrade_list[key]
		if lowest_value == None or level < lowest_value:
			lowest_value = level
			lowest_upgrade = key

def grass_upgrade():
	if grass_cost() < num_items(Items.Wood):
		print("Unlocking Grass Upgrade")
		unlock(Unlocks.Grass)

def pumpkin_upgrade():
	if pumpkin_cost() < num_items(Items.Carrot):
		print("Unlocking Pumpkin Upgrade")
		unlock(Unlocks.Pumpkins)

def carrot_upgrade():
	if carrot_cost() < num_items(Items.Wood):
		print("Unlocking Carrot Upgrade")
		unlock(Unlocks.Carrots)

def tree_upgrade():
	if tree_cost() < num_items(Items.Hay):
		print("Unlocking Tree Upgrade")
		unlock(Unlocks.Trees)

def speed_upgrade():
	if speed_cost() < num_items(Items.Hay):
		print("Unlocking Speed Upgrade")
		unlock(Unlocks.Speed)

def fertilizer_upgrade():
	if fertilizer_cost() < num_items(Items.Wood):
		print("Unlocking Fertilizer Upgrade")
		unlock(Unlocks.Fertilizer)

def watering_upgrade():
	if fertilizer_cost() < num_items(Items.Wood):
		print("Unlocking Watering Upgrade")
		unlock(Unlocks.Watering)

def cactus_upgrade():
	if cactus_cost() < num_items(Items.Pumpkin):
		print("Unlocking Cactus Upgrade")
		unlock(Unlocks.Cactus)

# Upgrades List
# Auto_Unlock
# Benchmark
# Cactus
# Costs
# Debug
# Debug_2
# Dictionaries
# Dinosaurs
# Expand
# Functions
# Leaderboard
# Lists
# Loops
# Mazes
# Multi_Trade
# Operators
# Plant
# Polyculture
# Senses
# Utilities
# Variables
