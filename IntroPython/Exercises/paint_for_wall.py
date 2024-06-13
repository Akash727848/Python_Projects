import math
def paint(h,w,c):
    nc=math.ceil(h*w/c)
    print(f"we can use {nc} number of cans for {h*w} sq.mtrs")
h=int(input("enter the height of the wall in meters: "))
w=int(input("enter the width of the wall in meters: "))
c=7
paint(h,w,c)