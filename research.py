import turtle
import math

def pattern(my_turtle, move):
    start_pos = my_turtle.pos()
    total_moves = []
    has_reached_first_time = False
    move_count = 0  # To keep track of the number of moves

    for i in move:
        my_turtle.forward(i)
        my_turtle.right(i)
        
        current_pos = my_turtle.pos()
        distance = math.sqrt((current_pos[0] - start_pos[0])**2 + (current_pos[1] - start_pos[1])**2)
        
        # Update move count
        move_count += 1
        
        # Skip the first 10 moves for stopping condition
        if move_count <= 10:
            total_moves.append(i)
            continue
        
        # Check if the turtle is within 9 units of the starting position after the first 10 moves
        if not has_reached_first_time and distance <= 9:
            has_reached_first_time = True
            total_moves.append(i)
            continue  # Continue to next move

        if has_reached_first_time and distance <= 9:
            total_moves.append(i)
            break
        
        total_moves.append(i)
    
    # Calculate circumference, radius, diameter, and area
    circumference = sum(total_moves)
    print("circumference =", circumference, "unit", sep=" ")
    
    radius = circumference / (2 * math.pi)
    print("radius =", radius, "unit", sep=" ")
    
    diameter = 2 * radius
    print("diameter =", diameter, "unit", sep=" ")
    
    area = math.pi * (radius ** 2)
    print("area =", area, "unit", sep=" ")
    
    # Convert all to cm (1 unit = 0.026458 cm)
    circumference_cm = circumference * 0.026458
    radius_cm = radius * 0.026458
    diameter_cm = diameter * 0.026458
    area_cm = area * (0.026458 ** 2)
    
    print(f"{circumference_cm} cm")
    print(f"{radius_cm} cm")
    print(f"{diameter_cm} cm")
    print(f"{area_cm} cm^2")
    
    print("Total moves used:", len(total_moves))
