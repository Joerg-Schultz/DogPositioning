positions = {
    "base": (3.6, 5.1),
    "back": (4.5, 2.4),
    "left": (0.4, 4.5),
    "right": (6.4, 6.2),
    "handler": (2.3, 9.9)
}

# A4 210 x 297 mm
# Drawing should be from 0m to 10m => 1m = 210/10 = 21 pixel
for (name, xy_pos) in positions.items():
    new_pos = (round(xy_pos[0] * 21), round(xy_pos[1] * 21))
    print(f"{name}: ({new_pos[0]}, {new_pos[1]})")
