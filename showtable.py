import random, json, sys, os

strategy = [[(0) for j in range(10)] for i in range(26)]
actions= [104,115,100]
display_act=["H","S","D"]




with open(sys.argv[1], "r") as f:
	strategy =  json.load(f)
f.closed
#print(strategy)
for i in range(26):	
	for j in range(10):
		os.write(1, bytes(display_act[actions.index(strategy[i][j])],'UTF-8'))
	print("")
	if i==16 :print()	
	