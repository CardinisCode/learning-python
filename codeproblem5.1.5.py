from math import atan2, degrees, radians, sin, cos

#Last problem, you created a new class called Force. Copy that
#class below:
class Force: 
    def __init__(self, magnitude, angle): 
        self.magnitude = magnitude
        self.angle = radians(angle)
    def get_horizontal(self): 
        return self.magnitude * cos(self.angle)
    def get_vertical(self):
        return self.magnitude * sin(self.angle)
    def get_angle(self, use_degrees=True):
        if use_degrees==True:
            self.angle = degrees(self.angle)
        else: 
            self.angle = radians(self.angle)
        return self.angle


#In this problem, you're going to use that class to calculate
#the net force from a list of forces.
#
#Write a function called find_net_force. find_net_force should
#have one parameter: a list of instances of Force. The
#function should return new instance of Force with the total
#net magnitude and net angle as the values for its magnitude
#and angle attributes.
#
#As a reminder:
#
# - To find "the magnitude of the net force", sum all the
#   horizontal components and sum all the vertical components.
#   The net force is the square root of the sum of the squares
#   of the horizontal forces and the vertical foces (i.e.
#   (total_horizontal ** 2 + total_vertical ** 2) ** 0.5)
# - To find the angle of the net force, call atan2 with two
#   arguments: the total vertical and total horizontal
#   forces (in that order).
# - Remember to round both the magnitude and direction to one
#   decimal place. This can be done using round(magnitude, 1)
#   and round(angle, 1).
# - The Force class has three methods: get_horizontal returns
#   a single force's horizontal component. get_vertical
#   returns a single force's vertical component. get_angle
#   returns a single force's angle in degrees (or in radians
#   if you call get_angle(use_degrees = False).
#
#HINT: Don't overcomplicate this. The Force class does a lot
#of your work for you. Use it! You should not need any trig
#functions except atan2, degrees, and radians.


#Add your function here!
def find_net_force(force_instances):
    total_horizontal = 0
    total_vertical = 0

    for instance in force_instances:
        magnitude = instance.magnitude
        print("The magnitude:", magnitude)
        angle = instance.get_angle()
        print("The angle:", angle)
        horizontal = instance.get_horizontal()
        print("horizontal:", horizontal)
        vertical = instance.get_vertical()
        print("vertical:", vertical)
        total_horizontal += horizontal
        total_vertical += vertical
        print()

    magnitude_of_the_net_force = (total_horizontal ** 2 + total_vertical ** 2) ** 0.5
    print("total_horizontal:", total_horizontal)
    print("total_vertical:", total_vertical)
    net_force = (total_horizontal ** 2 + total_vertical ** 2) ** 0.5
    angle_of_net_force = atan2(total_vertical, total_horizontal)

    magnitude = round(magnitude_of_the_net_force, 1)
    angle = round(angle_of_net_force, 1)
    angle = degrees(angle)
    print("Net magnitude:", magnitude)
    print("Net angle:", angle)


#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print:
#103.1
#-14.0
print()
force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
#print(net_force.magnitude)
#print(net_force.get_angle())



