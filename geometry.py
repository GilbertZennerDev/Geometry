import math
import random as r

def area_circle(radius):
    return (math.pi * radius**2)

def volume_box(width, length, height):
    return (width * length * height)

def volume_cube(side):
    return volume_box(side, side, side)

def distance_points(p1_x, p1_y, p2_x, p2_y):
    return math.sqrt((p2_x - p1['y'])**2 + (p2['x'] - p1['x'])**2)

def gen_point():
    return {
	'x': r.randint(-10, 10),
 	'y': r.randint(-10, 10),
}


print('Geometry:')
print('Area of circle of radius 2:', area_circle(2))
print('Volume of cube of side 2:', volume_cube(2))
print('Distance between two points:', distance_points(gen_point(), gen_point))
