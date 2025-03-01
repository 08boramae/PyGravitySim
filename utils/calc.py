def calcGravity(height, time, gravity=9.8):
    # Distance fallen = 1/2 * g * t^2
    distance_fallen = 0.5 * gravity * (time ** 2)
    new_height = height - distance_fallen
    
    # Velocity = g * t
    velocity = gravity * time
    
    # Ensure height doesn't go below 0
    return {
        "height": max(0, new_height),
        "velocity": velocity
    }