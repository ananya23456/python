from graphics.rectangle import *
from graphics.circle import *
from graphics.threeDgraphics.cuboid import *
from graphics.threeDgraphics.sphere import *

print("Rectangle area:", area1(10, 5))
print("Rectangle perimeter:", perimeter1(10, 5))

print("Circle area:", area(7))
print("Circle perimeter:", perimeter(7))

print("Cuboid surface area:", surface_area1(10, 5, 3))
print("Cuboid volume:", volume1(10, 5, 3))

print("Sphere surface area:", surface_area(5))
print("Sphere volume:", volume(5))
