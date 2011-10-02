#!/usr/bin/env python

import random

x = 0
c = 7
while x == 0:
	a = random.choice(range(1,c))
	if a == 1:
		print "*boom* yay winner!"
		print "Would you like to play again?"
		ans = int(raw_input("1 for yes, 0 for no: "))
		print ""
		if ans == 1:
			print "TOO BAD YOU'RE DEAD."
			print ":)"
			exit()
                elif ans == 0:
                        print "THE DEAD CANNOT SPEAK."
                        exit()
		else:
			print "Wrong answer, you dumb shit."
			exit()
	else:
		print "*click*"
		print "Would you like to play again?"
		ans = int(raw_input("1 for yes, 0 for no: "))
		print ""
		if ans == 1:
			x = 0
			c = c - 1
                elif ans == 0:
                    print "Coward."
                    exit()
		else:
			print "Wrong answer, you dumb shit."
			exit()
