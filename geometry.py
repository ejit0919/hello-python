import math


def triangle_perimeter (a, b, c):
      return a+b+c

def triangle_heronsarea (a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_circle(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    print("This is from geomtery.py")