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

# Gravity and bounce simulation parameters
simulation_time = 0
time_step = 0.1  # seconds per step
initial_height_from_ground = ground_level - initial_height
current_height_from_ground = initial_height_from_ground
current_velocity = 0
last_bounce_time = 0
bounce_count = 0
restitution = 0.7  # Coefficient of restitution (0.7 = 70% energy retained after bounce)

while True:
    simulation_time += time_step
    
    # Calculate physics (gravity effect)
    physics = calc.calcGravity(
        current_height_from_ground, 
        simulation_time, 
        current_velocity, 
        last_bounce_time
    )
    
    new_height_from_ground = physics["height"]
    velocity = physics["velocity"]
    acceleration = 9.8  # gravity constant
    
    # Handle bouncing
    if new_height_from_ground <= 0 and abs(velocity) > 0.5:  # Only bounce if velocity is significant
        # Object hit the ground, apply bounce
        bounce_count += 1
        last_bounce_time = simulation_time
        current_velocity = -velocity * restitution  # Reverse velocity with energy loss
        new_height_from_ground = 0  # Reset height to ground level
    else:
        current_velocity = velocity
    
    current_height_from_ground = new_height_from_ground
    
    # Convert to map coordinates (y=0 is top)
    new_y_pos = ground_level - int(new_height_from_ground)
    
    # Check boundaries
    if new_y_pos >= ground_level:
        new_y_pos = ground_level - 1  # Just above ground
    if new_y_pos < 0:
        new_y_pos = 0
        
    # Remove object from old position
    map.current_map[x + current_y_pos * map.MAP_WIDTH] = " "
    
    # Place object at new position
    current_y_pos = new_y_pos
    map.current_map[x + current_y_pos * map.MAP_WIDTH] = "o"
    
    print("\033[H\033[J")  # Clear screen
    print(f"Time: {simulation_time:.1f}s")
    map.print_map()
    print(f"Height: {new_height_from_ground:.2f}m")
    print(f"Velocity: {current_velocity:.2f}m/s (negative = upward)")
    print(f"Acceleration: {acceleration:.2f}m/s²")
    print(f"Bounce count: {bounce_count}")
    
    # Stop if object barely moves (simulation complete)
    if bounce_count > 0 and abs(current_velocity) < 0.5 and new_height_from_ground < 0.1:
        print("Object came to rest after bouncing.")
        break
    
    # Control simulation speed
    time.sleep(0.1)