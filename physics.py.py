#PiusD'Ds
def velocity(distance,time):
    return distance/time

def force(mass,acceleration):
    return mass * acceleration

def work(force,distance):
    return force * distance

def power(workdone,time):
    return workdone/time

def potential_energy(mass,gravity,height):
    return mass * gravity * height

print("Pick a physics formula \n "
      "a. velocity \n "
      "b. force \n "
      "c. work \n "
      "d. power \n "
      "e. potential energy")

pick = input("enter formula: ")

if pick == 'a':
    distance = float(input("Enter Distance: "))
    time = float(input("Enter time: "))
    print(f'the velocity is {velocity(distance,time)} m/s')

elif pick == 'b':
    mass = float(input("Enter Mass: "))
    acceleration = float(input("Enter Acceleration: "))
    print(f'the force is {force(mass,acceleration)} m/s2')

elif pick == 'c':
    force = float(input("Enter Force: "))
    distance = float(input("Enter Distance: "))
    print(f'the work is {work(force, distance)}J')

elif pick == 'd':
    workdone = float(input("Enter Workdone: "))
    time = float(input("Enter time: "))
    print(f'the power is {power(workdone,time)}J')

elif pick == 'e':
    mass = float(input("Enter mass: "))
    gravity = float(input("Enter gravity: "))
    height = float(input("Enter height: "))
    print(f'the potential energy is {potential_energy(mass,gravity,height)}N')

else:
    print("Please choose within a to e")