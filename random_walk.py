import random

def simple_random_walk_1d(steps, starting_position=0):
    pos = starting_position
    values = [starting_position]
    for x in range(0,steps-1):
        if(random.random() < 0.5):
            pos += 1
        else:
            pos -= 1
        values.append(pos)
    return values

def simple_random_walk_2d(steps, starting_positionx=0, starting_positiony=0):
    posx = starting_positionx
    posy = starting_positiony
    values = []
    values.append([posx, posy])
    for x in range(0,steps-1):
        a = random.random()
        b = random.random()
        if(a < 0.5 and b < 0.5):
            posx += 1
        elif(a < 0.5 and b >= 0.5):
            posx -= 1
        elif(a >= 0.5 and b < 0.5):
            posy += 1
        else:
            posy -= 1
        values.append((posx,posy))
    return values
