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
	
#############################################

# Planting Carrots
def carrot_plant_cost():
	cost_dict = get_cost(Entities.Carrot)
	for item in cost_dict:
		return cost_dict[item]

#############################################
# Upgrade Priorities
# 1 Grass
# 2 Carrots
# 3 Trees 
# 4 Pumpkins

# Contents
# Auto_Unlock
# Benchmark
# Cactus
# Carrots
# Costs
# Debug
# Debug_2
# Dictionaries
# Dinosaurs
# Expand
# Fertilizer
# Functions
# Grass
# Leaderboard
# Lists
# Loops
# Mazes
# Multi_Trade
# Operators
# Plant
# Polyculture
# Pumpkin
# Senses
# Speed
# Sunflowers
# Trees
# Utilities
# Variables
# Watering
