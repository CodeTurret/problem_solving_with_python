
import random
#random is a built in python function that generates random numbers.

def random_walk(n):
    """Return co-ordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        #we increase x and y value, based on 2-D graph quadrants
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x == x + 1
        else:
            x = x - 1

    return (x,y)    

           

#take a random walking steps
for i in range(25):
    walk = random_walk(10)
    #10 is the block number means each square box is 1, and we take 10 boxes
    print(walk, "Distance from home = ",
          abs(walk[0]) + abs(walk[1]))
