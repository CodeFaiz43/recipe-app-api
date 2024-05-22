"""_summary_
calculator function
"""
def add(x, y):

    """ Add two number and return result"""
    return x + y

def sub(x, y):
    
    """Subtracting number & return result"""

    if (x != 0 and y != 0 and x > y):
        return x - y
    else:
        return y - x
