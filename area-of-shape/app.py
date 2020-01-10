from datetime import date
from areaofcircle import area_of_circle
from areaofsquare import area_of_square
from areaoftriangle import area_of_triangle
from areaoftrapezium import area_of_trapezium
from areaofsphere import area_of_sphere

shape = ""
while shape != "end":
    shape = input("Please select a shape: ")
    if shape == "circle":
        r = float(input("please enter length of radius: "))
        area_of_circle(r)
    elif shape == "square":
        h = float(input("Please enter height: "))
        w = float(input("Please enter width: "))
        area_of_square(h, w)
    elif shape == "triangle":
        h = float(input("Please enter height: "))
        w = float(input("Please enter width: "))
        area_of_triangle(h, w)
    elif shape == "trapezium":
        a = float(input("Please enter first perpendicular side: "))
        b = float(input("Please enter second perpendicular side: "))
        h = float(input("Please enter height: "))
        area_of_trapezium(a, b, h)
    elif shape == "sphere":
        r = float(input("Please enter radius: "))
        area_of_sphere(r)


