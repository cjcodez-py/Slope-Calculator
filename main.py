print("----- Slope Calculator Initialized ------")
botname = "Slopey"
point1x = int(input(f"{botname}: Please enter your first point's X value.  "))
point1y = int(input(f"{botname}: Please enter your first point's Y value.  "))
point2x = int(input(f"{botname}: Now, Please enter your second point's X value.  "))
point2y = int(input(f"{botname}: Finally, enter your second point's Y value.  "))
slope = (point2y - point1y) / (point2x - point1x)
yint = point1y - slope * point1x
if point2x - point1x == 0:
    slope = "Undefined"
print(f"{botname}: Your slope is {slope}")
print(f"{botname}: Your Y-Intercept is {yint}")