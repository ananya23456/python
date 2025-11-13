from graphics.rectangle import area, perimeter
from graphics.circle import area as c_area, perimeter as c_perimeter
from graphics.threeDgraphics.cuboid import surface_area, volume
from graphics.threeDgraphics.sphere import surface_area as s_area, volume as s_volume

print("Rectangle area:", area(10, 5))
print("Rectangle perimeter:", perimeter(10, 5))

print("Circle area:", c_area(7))
print("Circle perimeter:", c_perimeter(7))

print("Cuboid surface area:", surface_area(10, 5, 3))
print("Cuboid volume:", volume(10, 5, 3))

print("Sphere surface area:", s_area(5))
print("Sphere volume:", s_volume(5))
