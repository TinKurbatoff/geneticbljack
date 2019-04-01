import random, json, math

strategy = [[(0) for j in range(10)] for i in range(26)]
actions= [104,115,100]

# mutation function for the next generation
def mutate(x, y, gen_num, gen_qty, gen_progress):
# x,y- number of good specie, gen_num - number of generation,
# gen_qty - quantity of species to born, gen_progress — 0..1 how mature is the generation ("1" - final gen)	
	mutate_treshold= 0.5*math.log(2-gen_progress)  # calculate the treshhold for random  mutation 0.15-0, logarithmic scale 
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
	 			if mutate_parameter < mutate_treshold:	strategy[a][b] = random.choice(actions) # mutate in "mutate_treshold" % of genes 
#	 			elif mutate_parameter < mutate_treshold+0.30:	strategy[a][b] = secnd_optimal_strategy[a][b] # mutate in 50%-30% genes with co-parent
	 			elif mutate_parameter < 0.50:	strategy[a][b] = secnd_optimal_strategy[a][b] # crossgenesis in 50% genes
	 			else:	# elitism — just copying genes of the best
	 				try: strategy[a][b] = optimal_strategy[a][b] # others just copy "genes"
	 				except IndexError: print("a:",a," b:",b)
	 	with open("./species/specie"+str(i)+".json", "w") as f:
	 		json.dump(strategy,f) # record next specie
	 	f.closed	