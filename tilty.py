# A simple MicroBit game by Giles Booth
# Tilt and colour in all the squares
# If you win level 20, press reset button to play again

from microbit import display, accelerometer, sleep, Image
from music import play, POWER_UP, NYAN

def get_xy():
    yaccel = accelerometer.get_y() * accelerometer_sensitivity
    xaccel = accelerometer.get_x() * accelerometer_sensitivity
    return yaccel, xaccel

def count_lit_pixels():
    pixel_count = 0
    for xx in range (5):
        for yy in range (5):
            if display.get_pixel(xx, yy) != 0:
                pixel_count += 1
    return pixel_count

pause = 100
level = 1
accelerometer_sensitivity=1/300

#set initial position    
x, y = 2, 2
yaccel, xaccel = get_xy()
y = max(0, min(4, int(y + yaccel)))
x = max(0, min(4, int(x + xaccel)))

while pause > 0:
    yaccel, xaccel = get_xy()
    newy = max(0, min(4, int(y + yaccel)))
    newx = max(0, min(4, int(x + xaccel)))
    if newy != y or newx != x:
        display.set_pixel(x, y, 1)
        x, y = newx, newy
        display.set_pixel(x, y, 9)
    else:
        display.set_pixel(newx, newy, 9)
    pixels = count_lit_pixels() 
    if pixels == 25:
        play(POWER_UP, wait=False)
        level += 1
        pause -= 5
        sleep(200)
        display.show(str(level))
        sleep(1000)
        display.clear()
    sleep(pause)
    
play(NYAN, wait=False)
display.show('WIN!')
sleep(200)
display.show(Image.HEART)
