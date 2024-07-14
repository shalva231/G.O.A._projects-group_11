# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    if integers[0]**2+integers[1]**2==integers[2]**2 or integers[1]**2+integers[2]**2==integers[0]**2 or integers[2]**2+integers[0]**2==integers[1]**2:
        return True
    else:
        return False