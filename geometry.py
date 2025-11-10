import math

def area_circle(radius):
    return (math.pi * radius**2)

def volume_box(width, length, height):
    return (width * length * height)

def volume_cube(side):
    return volume_box(side, side, side)

print('Geometry:')
print('Area of circle of radius 2:', area_circle(2))
print('Volume of cube of side 2:', volume_cube(2))

