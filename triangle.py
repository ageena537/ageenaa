'''
A program that accepts the lengths of three sides of a triangle as inputs. The program should output
whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right
triangle, the square of one side equals the sum of the squares of the other two sides).
Implement using functions.
'''
def check_right_angle(sides):
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False

sides=[]
sides.append(int(input("Enter the first side:")))
sides.append(int(input("Enter the second side:")))
sides.append(int(input("enter the third side:")))
if check_right_angle(sides):
    print("The sides are part of a right triangle")
else:
    print("The given sides are not a part of right triangle")
