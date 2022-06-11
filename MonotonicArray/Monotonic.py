def isMonotonic(array):
    #if len only 2 or less, there isn't enough values to cause both increasing and decreasing directions
    if len(array) <= 2:
        return True

    #gives first instancec of direction
    direction = array[1] - array[0]
    

    for i in range(2, len(array)):
        #generate direction on curent values of the loop 
        currentdir = array[i] - array[i - 1]
        
        #catches values that aren't increasing or decreasing
        if direction == 0:
            direction = currentdir
            continue
        
        #if true, the direction is opposed on currentdir and previous direction
        if checkDirections(direction, currentdir):
            return False

    # end of loop so no opposite directions found so return True
    return True
        
#helper function to check the directions 
def checkDirections(dir, curr):
    if dir > 0:
        return curr < 0
    return curr > 0


