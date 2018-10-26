import geometry

data = input("Enter the side lengths of a triangle: ")
values = data.split(",")

a = float(values[0])
b = float(values[1])
c = float(values[2])

print("Perimeter: {:.2f}".format(geometry.triangle_perimeter(a,b,c)))
print("Area: {:.2f}".format(geometry.triangle_heronsarea(a,b,c)))