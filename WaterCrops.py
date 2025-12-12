def water_crops():
	if get_water() < 0.76:
		use_item(Items.Water) 
			
def fertilize_crops():
	if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)

def fertilize_sunflowers():
	if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)
			use_item(Items.Fertilizer)
			use_item(Items.Weird_Substance)			