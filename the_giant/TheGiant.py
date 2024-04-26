import random
import math

class vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def len(self):
        return (self.x**2 + self.y**2)**.5
    
    def __str__(self):
        return f'{self.x} {self.y}'
    
    def angle(self, other):
        return (math.acos((self*other)/(self.len()*other.len())))*(180/math.pi)


def cross_product(p1, p2, p3):
    return (p2.x-p1.x)*(p3.y-p1.y) - (p2.y-p1.y)*(p3.x-p1.x)

def is_obtuse(p1, p2, p3):
    # Check if the points are on the same line
    if cross_product(p1, p2, p3) == 0:
        return False
    

    # Check if the points have an obtuse angle
    d1 = (p2-p1) * (p3-p1)
    d2 = (p1-p2) * (p3-p2)
    d3 = (p2-p3) * (p1-p3)
    if d1 < 0 or d2 < 0 or d3 < 0:
        return True
    return False

def is_obtuse_angle(p1, p2, p3):
    try:    
        angle1 = (p2-p1).angle(p3-p1)
        angle2 = (p1-p2).angle(p3-p2)
        angle3 = (p2-p3).angle(p1-p3)
    except(ZeroDivisionError):
        return False
    
    if cross_product(p1, p2, p3) == 0:
        return False
    
    if angle1 >= 91 or angle2 >= 91 or angle3 >= 91:
        return True

    return False

n, m = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

vec_1 = vec(x1, y1)
vec_2 = vec(x2, y2)

half_dist = int(math.ceil((vec_2-vec_1).len()))

max_x = min(max(x1, x2) + half_dist, n)
min_x = max(min(x1, x2) - half_dist, 0)
max_y = min(max(y1, y2) + half_dist, m)
min_y = max(min(y1, y2) - half_dist, 0)
p = vec(random.randint(min_x, max_x), random.randint(min_y,max_y))

while not is_obtuse_angle(p, vec_1, vec_2):
    p = vec(random.randint(min_x, max_x), random.randint(min_y,max_y))

print(p)