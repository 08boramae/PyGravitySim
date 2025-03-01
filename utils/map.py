# Define map constants
MAP_WIDTH = 10
MAP_HEIGHT = 20
GROUND_LEVEL = 19  # The y-coordinate where ground starts (0-based, must be < MAP_HEIGHT)

# Initialize empty map
current_map = [" " for _ in range(MAP_WIDTH * MAP_HEIGHT)]

# Set the ground level with "=" characters
for i in range(MAP_WIDTH):
    current_map[i + GROUND_LEVEL * MAP_WIDTH] = "="

def print_map():
    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
            print(current_map[x + y * MAP_WIDTH], end="")
        print("|")
    print("+" + "-" * MAP_WIDTH + "+")

def clear_map():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if y != GROUND_LEVEL:  # Don't clear the ground
                current_map[x + y * MAP_WIDTH] = " "
            else:
                current_map[x + y * MAP_WIDTH] = "="

def get_ground_level():
    return GROUND_LEVEL

def is_valid_position(x, y):
    return 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT