# This function calculates the total weight of two teams.
def row_weights(array):
    # Calculate the total weight of team 1 by summing the weights of every second player (index 0, 2, 4, etc.).
    team1 = sum(array[::2])
    # Calculate the total weight of team 2 by summing the weights of every second player (index 1, 3, 5, etc.).
    team2 = sum(array[1::2])
    
    # Return a tuple containing the total weight of team 1 and team 2.
    return (team1, team2)