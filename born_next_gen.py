import random, json

strategy = [[(0) for j in range(10)] for i in range(26)]
actions= [104,115,100]


def mutate(x, y, gen_num, gen_qty): # x,y- number of good specie, gen_num - number of generation, gen_qty - quantity of species to born
	with open("./species/specie"+str(x)+".json", "r") as f:
		optimal_strategy =  json.load(f)
	f.closed
	with open("./species/specie"+str(y)+".json", "r") as f:
		secnd_optimal_strategy =  json.load(f)
	f.closed

	with open("./species/gen"+str(gen_num)+".json", "w") as f:
		json.dump(optimal_strategy,f) # record a specie from current generation
	f.closed
	for i in range(gen_qty): # fill out all 100 species with new generation
	 	for a in range(26):	
	 		for b in range(10):
	 			mutate_parameter = random.random()
	 			if mutate_parameter < 0.05:	strategy[a][b] = random.choice(actions) # mutate in 5% genes
	 			elif mutate_parameter < 0.30:	strategy[a][b] = secnd_optimal_strategy[a][b] # mutate in 30% genes with pair
	 			else:	
	 				try: strategy[a][b] = optimal_strategy[a][b] # others just copy
	 				except IndexError: print("a:",a," b:",b)
	 	with open("./species/specie"+str(i)+".json", "w") as f:
	 		json.dump(strategy,f) # record next specie
	 	f.closed	