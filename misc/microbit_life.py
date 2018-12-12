# Conways game of life for BBC:microbit
# Twitter @hackerfantastic
import random
import microbit

def game_of_life():
	genrange = 10
	cellcount = 5,5
	state = {}
	# generate a random life state
	for row in range(cellcount[0]):
		for col in range(cellcount[1]):
			state["%d,%d" % (row,col)] = random.randint(0,1)
	## set a state 
	#state = {
	#	"0,0":0, "0,1":0,"0,2":0, "0,3": 0, "0,4": 0,
	#	"1,0":0, "1,1":0,"1,2":1, "1,3": 0, "1,4": 0,
	#	"2,0":0, "2,1":0,"2,2":1, "2,3": 0, "2,4": 1,
	#	"3,0":0, "3,1":0,"3,2":1, "3,3": 1, "3,4": 0,
	#	"4,0":0, "4,1":0,"4,2":0, "4,3": 0, "4,4": 0,
	#	}
	for generation in range(genrange):
		for row in range(cellcount[0]):
			for col in range(cellcount[1]):
				mystate = state["%d,%d" % (row,col)]
				if mystate == 1:
					microbit.display.set_pixel(col,row,9)
				else:
					microbit.display.set_pixel(col,row,0)
					
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
		microbit.sleep(500)
		
# main loop
game_of_life()
while True:
    if microbit.button_a.is_pressed():
        game_of_life()
    microbit.sleep(100)
