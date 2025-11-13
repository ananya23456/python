import graphics.rectangle
import graphics.circle
import graphics.threeDgraphics.cuboid as cuboid
import graphics.threeDgraphics.sphere as sphere

print("Rectangle area:", graphics.rectangle.area(10, 5))
print("Rectangle perimeter:", graphics.rectangle.perimeter(10, 5))

print("Circle area:", graphics.circle.area(7))
print("Circle perimeter:", graphics.circle.perimeter(7))

print("Cuboid surface area:", cuboid.surface_area(10, 5, 3))
print("Cuboid volume:", cuboid.volume(10, 5, 3))

print("Sphere surface area:", sphere.surface_area(5))
print("Sphere volume:", sphere.volume(5))
