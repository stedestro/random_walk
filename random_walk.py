import random

def simple_random_walk_1d(steps, starting_position=0):
    """
    Simple random walk in 1 dimension (up/down)

    Arguments:
        steps (int): number of steps
        starting_position: where does the walker starts

    Returns:
        List of 1d coordinates
    """
    pos = starting_position
    values = [starting_position]
    for x in range(0,steps-1):
        if(random.random() < 0.5):
            pos += 1
        else:
            pos -= 1
        values.append(pos)
    return values

def random_walk_1d(steps, starting_position=0.0, up_ratio=0.5, step_size=1.0):
    """
    Parametrable random walk in 1 dimension (up/down)

    Arguments:
        steps (int): number of steps
        starting_position (float): where does the walker starts
        up_ratio (float between 0 and 1.0): percentage of the steps going up
        step_size (float or tuple): How fat the step goes
            if step_size is a tuple, randomly select size between
            [step_size[0], step_size[1]]

    Returns:
        List of 1d coordinates
    """
    pos = starting_position
    values = [starting_position]
    for x in range(0,steps-1):
        if(random.random() < up_ratio):
            if isinstance(step_size, tuple):
                pos += random.uniform(step_size[0], step_size[1])
            else:
                pos += step_size
        else:
            if isinstance(step_size, tuple):
                pos -= random.uniform(step_size[0], step_size[1])
            else:
                pos -= step_size
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
