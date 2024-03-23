import random as rnd

def random_walk(n):
    """Return coordinates of a random walk of 'n' blocks."""
    x, y = 0, 0
    for i in range(n):
        dir = rnd.choice(['North', 'South', 'East', 'West'])
        if dir == 'East':
            x += 1
        elif dir == 'West':
            x -= 1
        elif dir == 'South':
            y -= 1
        else:
            y += 1
    return (x, y)

def random_walk_2(n):
    """Return coordinates of a random walk of 'n' blocks."""
    x, y = 0, 0
    for i in range(n):
        dx, dy = rnd.choice([(0,1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

number_of_walks = 20000
for walk_length in range(1, 31):
    no_transport = 0 # number of walks <= 4 blocks
    for i in range(number_of_walks):
        dest = random_walk_2(walk_length)
        dth = abs(dest[0]) + abs(dest[1])
        if dth <= 4:
            no_transport += 1
    no_transport_pct = float(no_transport) * 100.0 / float(number_of_walks)
    print("For a walk length of {n} you would not need transport home {pct:.1f}% of the time.".format(n=walk_length, pct=no_transport_pct))


