def firstDuplicateValue(array):

    # create catch variable that will append all values
    catch = []
    
    # looping throught each 
    for i in array:

      # unique char will be added
        if i not in catch:
            catch.append(i)
        
        # return first duplicate
        elif i in catch:
            return i
      
    # all unique char means no duplicates are found
    return -1

