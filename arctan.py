import math

n = 3.14159265

ax, ay, az, bx, by, bz = map(float, input("? ").split())

ka = math.atan2(bx - ax, by - ay)
print("Azimuth K =", ka)

if ka < 0:
    print("Adding 2PI to K...")
    ka += 2 * PI

azu = ka * (180 / n)
print("Azimuth =", azu)

ke = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
print("\nElevation K =", ke)

ele = math.atan((bz - az) / ke) * 180 / n
print("Elevation =", ele)
