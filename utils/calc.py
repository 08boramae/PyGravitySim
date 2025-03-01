def calcGravity(height, time, velocity=0, last_bounce_time=0, gravity=9.8):
    # Time since last bounce
    elapsed_since_bounce = time - last_bounce_time
    
    # Calculate velocity: v = v0 + g*t
    current_velocity = velocity + gravity * elapsed_since_bounce
    
    # Calculate height: h = h0 + v0*t + 0.5*g*t^2
    new_height = height - (velocity * elapsed_since_bounce + 0.5 * gravity * (elapsed_since_bounce ** 2))
    
    return {
        "height": max(0, new_height),
        "velocity": current_velocity,
        "last_bounce_time": last_bounce_time
    }