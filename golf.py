import random
import math
import numpy as np

#random weather generator
def gen_weather():
    
    weather = {}
    speed = random.randint(0,100)
    weather['Wind Speed'] = speed
    dir = random.choice(range(9))
    
    match dir:
        case 0:
            weather['Wind Direction'] = 'N'
            weather['Wind Vector'] = [0, speed]
        case 1: 
            weather['Wind Direction'] = 'S'
            weather['Wind Vector'] = [0, -speed]
        case 2: 
            weather['Wind Direction'] = 'E'
            weather['Wind Vector'] = [speed, 0]
        case 3: 
            weather['Wind Direction'] = 'W'
            weather['Wind Vector'] = [-speed, 0]
        case 5: 
            weather['Wind Direction'] = 'NE'
            weather['Wind Vector'] = [speed*math.cos(np.radians(45)), speed*math.cos(np.radians(45))]
        case 6: 
            weather['Wind Direction'] = 'NW'
            weather['Wind Vector'] = [speed*math.cos(np.radians(45)), -speed*math.cos(np.radians(45))]
        case 7: 
            weather['Wind Direction'] = 'SE'
            weather['Wind Vector'] = [-speed*math.cos(np.radians(45)), speed*math.cos(np.radians(45))]
        case 8: 
            weather['Wind Direction'] = 'SW'
            weather['Wind Vector'] = [-speed*math.cos(np.radians(45)), -speed*math.cos(np.radians(45))]
    
    return weather

#drive mode: 3d ballistic motion    
def drive(speed, direction, angle, old_spot, weather):
       
    new_spot = []
    roots = np.roots([-16.1, speed*math.sin(np.radians(angle)), 0])
    time = roots[0]
    print(time)
    print(speed)
    print(math.cos(np.radians(direction)))
    print(speed*math.sin(np.radians(direction))*time)
    
    new_spot.append(old_spot[0] + speed*math.sin(np.radians(direction))*math.cos(np.radians(angle))*time + weather['Wind Vector'][0]*time)
    new_spot.append(old_spot[1] + speed*math.cos(np.radians(direction))*math.cos(np.radians(angle))*time + weather['Wind Vector'][1]*time)

    return new_spot

#putt mode: based on kinetic friction
def putt(speed, direction):
    match direction:
        case 'N':
            direction = [speed, 0]
        case 'S':
            direction = [-speed, 0]
        case 'E':
            direction = [0, speed]
        case 'W':
            direction = [0, -speed]
        case 'NE':
            direction = [speed*math.cos(45), speed*math.cos(45)]
        case 'NW':
            direction = [speed*math.cos(45), -speed*math.cos(45)]
        case 'SW':
            direction = [-speed*math.cos(45), speed*math.cos(45)]
        case 'SE':
            direction = [-speed*math.cos(45), -speed*math.cos(45)]

def main():
    strokes = 0
    old_spot = [0,0]
    print('You are at coordinate point 0,0. The green is at 500,500 (NE)')
    weather = gen_weather()
    print("The wind is blowing", weather['Wind Direction'], "at" , weather['Wind Speed'], "feet per second.")
    while (True):
        mode = input(print('Putt or drive?'))
        mode = str.upper(mode)
        speed = float(input(print('Ball speed?')))
        direction = float(input(print('Degrees from north?')))
        angle = float(input(print('Launch angle?')))
        new_spot = drive(speed, direction, angle, old_spot, weather)
        
        if(new_spot[0] > 500-1 and new_spot[0] < 500 + 1 and new_spot[1] > 500 - 1 and new_spot[1] < 500 + 1 and strokes == 0):
            print("HOLE IN ONE")
            again = str.upper(input(print('Play again?')))
            if again == "Y":
                continue
            else: 
                break
        if(new_spot[0] > 500-1 and new_spot[0] < 500 + 1 and new_spot[1] > 500 - 1 and new_spot[1] < 500 + 1):
            print('Sunk')
            print('Strokes:', strokes)
            again = str.upper(input(print('Play again?')))
            if again == "Y":
                continue
            else: 
                break
        
        old_spot = new_spot
        strokes = strokes + 1
        
        print("You are now at coordinate point", old_spot)
    
     
main()







