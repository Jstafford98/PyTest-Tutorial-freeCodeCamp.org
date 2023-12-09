def add(x : int | float, y : int | float) -> int | float :
    return x + y

def divide(x : int | float, y  : int | float) -> int | float :
    
    if y == 0:
        raise ValueError
    
    return x / y