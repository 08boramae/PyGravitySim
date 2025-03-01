import time
from utils import map
from utils import calc

start_point = input("Enter the start point(like 1 3): ")
start_point = start_point.split(" ")
start_point = [int(start_point[0]), int(start_point[1])]

# Set initial position (y=0 is top of map)
x = start_point[0] 
initial_height = start_point[1]
current_y_pos = initial_height

# Set ground level on map
ground_level = map.get_ground_level()

# Cleear all map objects
map.clear_map()

# Place object at initial position
map.current_map[x + current_y_pos * map.MAP_WIDTH] = "o"

map.print_map()
print(f"Initial height: {ground_level-initial_height} (from ground)")

# Gravity simulation parameters
simulation_time = 0
time_step = 0.05  # seconds per step(0.1이 적당)

while True:
    simulation_time += time_step
    
    height_from_ground = ground_level - initial_height
    physics = calc.calcGravity(height_from_ground, simulation_time)
    new_height_from_ground = physics["height"]
    velocity = physics["velocity"]
    acceleration = 9.8  # gravity constant
    
    new_y_pos = ground_level - int(new_height_from_ground)
    
    if new_y_pos >= ground_level:
        new_y_pos = ground_level - 1  # Just above ground
    if new_y_pos < 0:
        new_y_pos = 0
        
    map.current_map[x + current_y_pos * map.MAP_WIDTH] = " "
    
    current_y_pos = new_y_pos
    map.current_map[x + current_y_pos * map.MAP_WIDTH] = "o"
    
    print("\033[H\033[J")  # Clear screen
    print(f"Time: {simulation_time:.1f}s")
    map.print_map()
    print(f"Height: {new_height_from_ground:.2f}m")
    print(f"Velocity: {velocity:.2f}m/s")
    print(f"Acceleration: {acceleration:.2f}m/s²")
    
    if current_y_pos >= ground_level - 1:
        print("Object hit the ground!")
        print(f"Impact velocity: {velocity:.2f}m/s")
        break
    
    # Control simulation speed
    time.sleep(0.1)