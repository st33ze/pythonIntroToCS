# cannonball.py
# This program simulates flight of the projectile, depending on the
# input from user, who gives angle, initial velocity, initial height
# and time interval. The output is position of the projectile from
# starting point.

from projectile import Projectile

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    maxHeight = h0
    while cball.getY() >= 0:
        if maxHeight < cball.getY():
            maxHeight = cball.getY()
        cball.update(time)
    print('Distance traveled: {:0.2f} meters.'.format(cball.getX()))
    print('Maximum height: {:0.2f} meters.'.format(maxHeight))


def getInputs():
    ''' Promts user for inputs, verifies and returns them '''
    inputFormat = 0

    # Veryfy Angle
    while True:
        angle = checkFormat(input('Initial angle (int 0 - 90): '))
        if angle >= 0 and angle <= 90:
            break

    # Veryfy velocity
    while True:
        vel = checkFormat(input('Initial velocity m/s: '))
        if vel > 0:
            break

    # Veryfy initial height
    while True:
        h0 = checkFormat(input('Initial height (int 0 - 100): '))
        if h0 >= 0 and h0 <= 100:
            break

    # Veryfy time interval
    while True:
        time = checkFormat(input('Time interval in seconds: '))
        if time > 0:
            break

    return angle, vel, h0, time

def checkFormat(input):
    ''' Checks the input and returns evaluated format '''
    try:
        input = int(input)
    except:
        try:
            input = float(input)
        except:
            input = -1

    return input





if __name__ == '__main__':
    main()
