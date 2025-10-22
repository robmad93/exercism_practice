def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if 0 in sides or a < 0 or b < 0 or c < 0:
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False
        
    if a == b == c:
        return True
    else:
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if 0 in sides or a < 0 or b < 0 or c < 0:
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False

    if a == b or b == c or a == c:
        return True
    else:
        return False
    


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if 0 in sides or a < 0 or b < 0 or c < 0:
        return False

    if not (a + b > c and a + c > b and b + c > a):
        return False

    if a != b and b != c and c != a:
        return True
    else:
        return False

    
    
