# Game of life in ascii
import random
import time
import os

def game_of_life():
	genrange = 1000  # number of generations
	cellcount = 50,50 # grid size
	state = {}
	# generate a random life state
	for row in range(cellcount[0]):
		for col in range(cellcount[1]):
			state["%d,%d" % (row,col)] = 0
	# make it mostly dead cells then live 
	for count in range(random.randint(0,500)):
		X = random.randint(0,cellcount[0])
		Y = random.randint(0,cellcount[1])
		state["%d,%d" % (X,Y)] = 1

	for generation in range(genrange):
		print "Generation %d" % generation
		for row in range(cellcount[0]):
			for col in range(cellcount[1]):
				mystate = state["%d,%d" % (row,col)]
			#	if mystate == 1:
			#	    microbit.display.set_pixel(row,col,9)
			#	else:
			#		microbit.display.set_pixel(row,col,0)
				if mystate == 1:
					print "o",
				else:
					print " ",
			print ""
		for row in range(cellcount[0]):
			for col in range(cellcount[1]):
				moore = 0
				try:
					moore = moore + state["%d,%d" % (row+1,col-1)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row+1,col)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row+1,col+1)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row,col-1)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row,col+1)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row-1,col-1)]
				except:
					moore = moore + 0	
				try:
					moore = moore + state["%d,%d" % (row-1,col)]
				except:
					moore = moore + 0
				try:
					moore = moore + state["%d,%d" % (row-1,col+1)]
				except:
					moore = moore + 0
				oldstate = state["%d,%d" % (row,col)]
				# rules
				#C   N                 new C
				#1   0,1             ->  0  # Lonely
				#1   4,5,6,7,8       ->  0  # Overcrowded
				#1   2,3             ->  1  # Lives
				#0   3               ->  1  # It takes three to give birth!
				#0   0,1,2,4,5,6,7,8 ->  0  # Barren
				if oldstate == 0:
					if moore == 3:
						newstate = 1
					else:
						newstate = 0
				if oldstate == 1:
					if moore == 0 or moore == 1:
						newstate = 0
					if moore >= 4 and moore <= 8:
						newstate = 0
					if moore == 2 or moore == 3:
						newstate = 1
				state["%d,%d" % (row,col)] = newstate
				moore = 0
		os.system("clear")
		
# main loop
if __name__ == "__main__":
	game_of_life()
