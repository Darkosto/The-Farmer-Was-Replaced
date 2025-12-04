hat_equipped = 0

hat_type = [
	Hats.Brown_Hat, 			# 0
	Hats.Brown_Hat, 			#1
	Hats.Cactus_Hat, 			#2
	Hats.Carrot_Hat, 			#3
	Hats.Dinosaur_Hat,		  #4
	Hats.Gold_Hat,			   	#5	
	Hats.Gray_Hat, 				#6	
	Hats.Green_Hat,				#7		
	Hats.Pumpkin_Hat,			#8		
	Hats.Purple_Hat, 			#9		
	Hats.Straw_Hat,				#10
	Hats.Tree_Hat,				#11
	Hats.Sunflower_Hat		#12
]

def wear_hat(index):
	global hat_equipped
	global hat_type_worn
	if 0 <= index < len(hat_type):
		change_hat(hat_type[index])
		hat_type_worn = index
		hat_equipped = 1
	else:
		print("Invalid hat index!")


#print(hat_type_worn)
#wear_hat(8)