def robot_position(n, m, commands):
    # Initial position of the robot is (0, 0)
    row, col = 0, 0
    
    # Directions map
    direction_map = {
        'UP': (-1, 0),    # Move up decreases row by 1
        'DOWN': (1, 0),   # Move down increases row by 1
        'LEFT': (0, -1),  # Move left decreases column by 1
        'RIGHT': (0, 1)   # Move right increases column by 1
    }
    
    # Process each command
    for command in commands:
        # Get the direction change for this command
        dr, dc = direction_map[command]
        
        # Update robot's position
        row += dr
        col += dc
        
        # Check if the new position is out of bounds
        if not (0 <= row < n and 0 <= col < n):
            return -1
    
    # Return the final position if all moves are valid
    return [row, col]

# Example input processing
n = int(input())  # Size of the grid (n x n)
m = int(input())  # Number of commands
commands = input().split()  # List of m commands

# Output the final position of the robot
print(robot_position(n, m, commands))
