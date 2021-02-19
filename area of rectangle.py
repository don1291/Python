length = float(input("Enter the length 1: "))
width = float(input("Enter the width 1: "))
length2 = float(input("Enter the length 2: "))
width2 = float(input("Enter the width 1: "))
area = length *width
area2 = length2 * width2
print(area,area2)

if area > area2:
    print("the first area is greater ")
if area < area2:
    print("The second area is greater")
if area == area2:
    print("the area is the same") 

