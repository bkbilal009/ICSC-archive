# ICSC 2026 - Problem B: Pixel Art Solution
# Submission Track: Computer Science (Qualification)

def generate_shape(n: int, shape: str) -> list:
    """
    Generates an N x N matrix populated with 0s and 1s based on the requested geometric shape.
    
    Parameters:
    n (int): The dimensions of the grid (N x N).
    shape (str): The pattern type ('checkerboard' or 'diamond').
    
    Returns:
    list: A 2D list representing the grid.
    """
    grid = [[0] * n for _ in range(n)]
    
    if shape == "checkerboard":
        for i in range(n):
            for j in range(n):
                # Parity of the combined coordinate indexes dictates spatial toggling
                # Top-left (0,0) evaluates to 0
                grid[i][j] = (i + j) % 2
                
    elif shape == "diamond":
        center = n // 2
        for i in range(n):
            for j in range(n):
                # Mathematical Manhattan distance threshold determines geometry boundary
                if abs(i - center) + abs(j - center) <= center:
                    grid[i][j] = 1
                    
    return grid

if __name__ == "__main__":
    # Example test cases
    print("Test Checkerboard (5x5):")
    for row in generate_shape(5, "checkerboard"):
        print(row)
        
    print("\nTest Diamond (5x5):")
    for row in generate_shape(5, "diamond"):
        print(row)
