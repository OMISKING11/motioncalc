import math
print("This program calculates the motion of any object just fill the correct values in the correct places and you are good to go.")
print("made by Om Kumar")
print("Which value you have to find out\n"
     "1. Final Velocity\n"
     "2. Initial Velocity\n"
     "3. Acceleration\n"
     "4. Time\n"
     "5. Distance")
ask = int(input("Enter the number of the value you want to find out: "))
def Final_Velocity():
    u = float(input("Enter the initial velocity: "))
    ucheck = input("Is the initial velocity in m/s(1) or km/h(2): ")
    if ucheck == 1:
        pass
    elif ucheck == 2:
        u = u * 5/18
    a = float(input("Enter the acceleration: "))
    t = float(input("Enter the time: "))
    v = u + a * t
    answer = int(input("You want the answer in m/s^2(1) or km/h^2(2): "))
    if answer == 1:
        print("The final velocity is", v + "m/s^2")
    else:
      v = v * 18/5
      print("The final velocity is", v + "km/hr")

def Initial_Velocity():
    v = float(input("Enter the final velocity: "))
    vcheck = input("Is the final velocity given in m/s(1) or km/h(2): ")
    if vcheck == 1:
      pass
    elif vcheck == 2:
      v = v * 5/18
    a = float(input("Enter the acceleration: "))
    t = float(input("Enter the time: "))
    u = v - a * t
    answer = int(input("You want the answer in m/s^2(1) or km/h^2(2): "))
    if answer == 1:
        print("The initial velocity is", u, "m/s^2")
    else:
      u = u * 18/5
      print("The initial velocity is", u, "km/hr")

def Acceleration():
    v = float(input("Enter the final velocity: "))
    vcheck = input("Is the final velocity given in m/s(1) or km/h(2): ")
    if vcheck == 1:
      pass
    elif vcheck == 2:
      v = v * 5/18
    u = float(input("Enter the initial velocity: "))
    ucheck = input("Is the initial velocity in m/s(1) or km/h(2): ")
    if ucheck == 1:
        pass
    elif ucheck == 2:
        u = u * 5/18
    t = float(input("Enter the time: "))
    a = (v - u) / t
    answer = int(input("You want the answer in m/s^2(1) or km/h^2(2): "))
    if answer == 1:
        print("The acceleration is", a + "m/s^2")
    else:
      a = a * 18/5
      print("The acceleration is", a + "km/hr^2")

def Time():
    print("with distance or not if yes 1 else 2")
    ask1 = int(input("Enter the number: "))
    if ask1 == 1:
      d = float(input("Enter the distance: "))
      dcheck = input("Is the distance given in m(1) or km(2): ")
      if dcheck == 1:
        pass
      elif dcheck == 2:
        d = d * 1000
      u = float(input("Enter the initial velocity: "))
      ucheck = input("Is the initial velocity in m/s(1) or km/h(2): ")
      if ucheck == 1:
        pass
      elif ucheck == 2:
        u = u * 5/18
      a = float(input("Enter the acceleration: "))
      t = math.sqrt(2 * d / (u + a))
      print("The time is", t, "seconds")
    else:
      v = float(input("Enter the final velocity: "))
      vcheck = input("Is the final velocity in m/s(1) or km/h(2): ")
      if vcheck == 1:
        pass
      elif vcheck == 2:
        v = v * 5/18
        print(v)
      u = float(input("Enter the initial velocity: "))
      ucheck = input("Is the initial velocity in m/s(1) or km/h(2): ")
      if ucheck == 1:
        pass
      elif ucheck == 2:
        u = u * 5/18
        print(u)
      a = float(input("Enter the acceleration: "))
      t = (v - u) / a
      print("The time is", t, "seconds")

def Distance():
    u = float(input("Enter the initial velocity: "))
    ucheck = input("Is the initial velocity in m/s(1) or km/h(2): ")
    if ucheck == 1:
        pass
    elif ucheck == 2:
        u = u * 5/18
    a = float(input("Enter the acceleration: "))
    t = float(input("Enter the time: "))
    d = (u * t) + (0.5 * a * t * t)
    print("The distance is", d, "meters")

if ask == 1:
    Final_Velocity()
elif ask == 2:
    Initial_Velocity()
elif ask == 3:
    Acceleration()
elif ask == 4:
    Time()
elif ask == 5:
    Distance()
