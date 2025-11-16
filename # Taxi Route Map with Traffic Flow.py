# Taxi Route Map with Traffic Flow

GRID_SIZE =15
# Symbols:
# T = Taxi start
# P = Passenger
# D = Destination
# * = Path taken
# X = Traffic (slows taxi)
def get_position(name):
    while True:
        try:
            pos = input(f"Enter {name} position as x,y (0 to {GRID_SIZE-1}): ")
            x, y = map(int, pos.split(','))
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                return (x, y)
            else:
                print("Position out of bounds, try again.")
        except:
            print("Invalid format, use x,y")
taxi_pos = get_position("Taxi start")
passenger_pos = get_position("Passenger pickup")
destination_pos = get_position("Destination drop-off")
# Traffic positions 
traffic = []
traffic_input = input("Enter traffic positions as x,y separated by space: ")
if traffic_input.strip():
    try:
        for t in traffic_input.strip().split():
            x, y = map(int, t.split(','))
            traffic.append((x, y))
    except:
        print("Invalid traffic positions, ignoring traffic.")
path = [taxi_pos]
def move_towards(curr, target):
    x, y = curr
    tx, ty = target
    if x < tx: x += 1
    elif x > tx: x -= 1
    elif y < ty: y += 1
    elif y > ty: y -= 1
    return (x, y)
# Move taxi to pickup
while taxi_pos != passenger_pos:
    taxi_pos = move_towards(taxi_pos, passenger_pos)
    path.append(taxi_pos)
# Move taxi to destination
while taxi_pos != destination_pos:
    taxi_pos = move_towards(taxi_pos, destination_pos)
    path.append(taxi_pos)
# ----- Draw Grid -----
grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for (x, y) in path:
    grid[y][x] = '*'
# Mark traffic
for (x, y) in traffic:
    grid[y][x] = 'X'
px, py = passenger_pos
dx, dy = destination_pos
grid[py][px] = 'P'
grid[dy][dx] = 'D'
sx, sy = path[0]
grid[sy][sx] = 'T'
print("\nTaxi Route Map:")
for row in grid:
    print(' '.join(row))
# ----- Calculate Time Considering Traffic -----
time = 0
for step in path[1:]:  # ignore starting point
    time += 2 if step in traffic else 1  # traffic takes 2 units, normal =1
print(f"\nTotal steps (considering traffic delay): {time}")
