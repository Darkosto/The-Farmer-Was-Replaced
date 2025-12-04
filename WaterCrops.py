def water_crops(a = True):
	if a:
		if get_water() < 0.76:
			use_item(Items.Water) 
			
def fertilize_crops():
	amount = num_items(Items.Fertilizer)
	return 0 < amount < 200000

					