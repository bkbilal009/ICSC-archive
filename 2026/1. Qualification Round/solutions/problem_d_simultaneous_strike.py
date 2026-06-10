# ICSC 2026 - Problem D: The Simultaneous Strike Solution
# Submission Track: Computer Science (Qualification)

def processGame(events: list, H: int) -> list:
    """
    Processes multi-player game events sequentially by frame, resolving 
    simultaneous attacks within the same frame before assessing death states.
    
    Parameters:
    events (list): List of tuples/lists containing (player_id, frame, damage)
    H (int): Initial maximum hit points (HP) for both players.
    
    Returns:
    list: Final health pool values [player1_hp, player2_hp] clamped to a minimum of 0.
    """
    if not events:
        return [H, H]
        
    # Enforce chronological ordering across historical event sequences based on frame index (element 1)
    sorted_events = sorted(events, key=lambda x: x[1])
    
    p1_hp = H
    p2_hp = H
    
    i = 0
    num_events = len(sorted_events)
    
    while i < num_events:
        # Evaluate death termination states prior to processing subsequent frame clusters
        if p1_hp <= 0 or p2_hp <= 0:
            break
            
        current_frame = sorted_events[i][1]
        frame_end_index = i
        
        # Look ahead to aggregate all matching continuous events within the same frame
        while frame_end_index < num_events and sorted_events[frame_end_index][1] == current_frame:
            frame_end_index += 1
            
        # Execute concurrent calculation modifications simultaneously for this frame cluster
        for idx in range(i, frame_end_index):
            player, _, attack = sorted_events[idx]
            if player == 1:
                p2_hp -= attack
            elif player == 2:
                p1_hp -= attack
                
        # Advance state pointer index to step past the current frame group
        i = frame_end_index
        
    # Apply lower floor normalization clamping across health metrics
    return [max(0, p1_hp), max(0, p2_hp)]

if __name__ == "__main__":
    # Example test matching simultaneous strike logs on frame 512
    sample_events = [
        [1, 512, 20],
        [2, 512, 20]
    ]
    print("Final HP State:", processGame(sample_events, 15))
