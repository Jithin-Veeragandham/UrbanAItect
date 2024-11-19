import random

def generate_city_grid(width, height, num_buildings, num_emergency_services):
    """
    Generates the city grid randomly. Places a given number of buildings and emergency services,
    and fills the rest of the grid with roads. Buildings are only placed in alternate rows.
    """
    print(f"Generating grid with {num_buildings} buildings and {num_emergency_services} emergency services...")
    total_cells = width * height
    remaining_cells = total_cells - num_buildings - num_emergency_services

    # Ensure we have enough room for roads and intersections
    if remaining_cells <= 0:
        raise ValueError("Too many buildings and emergency services for the grid size!")

    # Create the initial grid with roads (0) as placeholders
    grid = [[0] * width for _ in range(height)]

    # Determine which rows can have buildings (alternate rows: 0, 2, 4, ...)
    building_rows = [i for i in range(height) if i % 2 != 0]

    # Create a pool of possible positions for buildings and emergency services in the allowed rows
    available_positions = [(row, col) for row in building_rows for col in range(width)]

    # Check if there are enough positions to place all buildings and emergency services
    if len(available_positions) < num_buildings + num_emergency_services:
        raise ValueError("Not enough space to place all buildings and emergency services in alternate rows.")

    # Randomly select positions for buildings and emergency services
    selected_positions = random.sample(available_positions, num_buildings + num_emergency_services)

    # Assign the first 'num_buildings' positions to buildings (1) and the rest to emergency services (2)
    for idx, (row, col) in enumerate(selected_positions):
        if idx < num_buildings:
            grid[row][col] = 1  # Mark this spot with a building
        else:
            grid[row][col] = 2  # Mark this spot with an emergency service

    # Add intersections in columns randomly where possible
    for col in range(width):
        possible_rows = [row for row in range(height) if grid[row][col] == 0]
        if possible_rows:
            selected_row = random.choice(possible_rows)
            grid[selected_row][col] = 3  # Set this cell as an intersection

    # Increase the grid size to add borders of intersections
    width += 2
    height += 2

    # Create the new grid with intersections on the borders
    new_grid = [[3] * width]  # Top row of intersections
    for row in grid:
        new_grid.append([3] + row + [3])  # Add intersection columns to the left and right of each row
    
    new_grid.append([3] * width)  # Bottom row of intersections

    print("Grid generated:")
    for row in new_grid:
        print(row)
    
    return new_grid