def is_valid_walk(walk):
    location = [0,0]
    
    if len(walk)==10:
        for i in walk:
            if i == "n":
                location[0] += 1
            elif i == "s":
                location[0] -= 1
            elif i == "e":
                location[1] += 1
            elif i == "w":
                location[1] -= 1
        if location == [0,0]:
            return True
        else:
            return False
    else:
        return False