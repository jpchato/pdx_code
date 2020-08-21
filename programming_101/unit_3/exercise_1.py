import math

# 1.1
tri_side_1 = 1
tri_side_2 = 2
hypotenuse = (tri_side_1*tri_side_1 + tri_side_2*tri_side_2)


def triangle_perimeter(tri_side_1, tri_side_2, hypotenuse):
    print(tri_side_1 + tri_side_2 + hypotenuse)
    return tri_side_1 + tri_side_2 + hypotenuse

# 1.2
def triangle_area(tri_side_2, tri_side_1):
    print((tri_side_1*tri_side_2)/2)
    return (tri_side_1*tri_side_2)/2

#1.3
radius = 5
pi = math.pi
print(pi)
def circle_circumference(radius):
    print(int(radius*math.pi*2))
    return int(radius*math.pi*2)

# 1.4
def sphere_volume(radius):
    volume = (math.pi*radius*radius*radius*4)/3
    print (volume)
    return volume

# 1.5
radius_2 = 3
def annulus_area(radius, radius_2):
    area = int(math.pi*(radius*radius-radius_2*radius_2))
    print (area)
    return area
   


if __name__ == "__main__":
    triangle_perimeter(tri_side_1, tri_side_2, hypotenuse)
    triangle_area(tri_side_2, tri_side_1)
    circle_circumference(radius)
    sphere_volume(radius)
    annulus_area(radius, radius_2)
