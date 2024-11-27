def greedy_set_cover(universe, sets):
    # Initialize an empty list for the selected sets
    selected_sets = []
    
    # A set to track the covered elements
    covered_elements = set()
    
    # While there are uncovered elements
    while covered_elements != universe:
        # Find the set that covers the most uncovered elements
        best_set = None
        max_cover = 0
        
        for s in sets:
            # Count the number of uncovered elements in the current set
            uncovered_elements = len(s - covered_elements)
            if uncovered_elements > max_cover:
                max_cover = uncovered_elements
                best_set = s
        
        # Add the best set to the selected sets
        selected_sets.append(best_set)
        # Update the covered elements
        covered_elements.update(best_set)
        # Remove the selected set from the list of available sets
        sets.remove(best_set)
    
    return selected_sets

# Example usage
if __name__ == "__main__":
    # Universe of elements
    universe = {1, 2, 3, 4, 5, 6}
    
    # Collection of sets
    sets = [
        {1, 2, 3},
        {2, 3, 4},
        {3, 4, 5},
        {4, 5, 6},
        {1, 5}
    ]
    
    # Calling the greedy set cover algorithm
    selected_sets = greedy_set_cover(universe, sets)
    
    # Output the selected sets
    print("Selected sets:", selected_sets)
    print("Covered elements:", set().union(*selected_sets))  # Union of selected sets
