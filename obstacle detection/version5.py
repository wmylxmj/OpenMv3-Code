# Untitled - By: wmy - 周日 12月 2 2018

import sensor, image, time
from pyb import UART

warning_threshold   = (   75,   100,  -25,   25,   -25,   25)

kernel_size = 2
kernel = [-1, -1, -1, -1, -1,
          -1,  1,  1,  1, -1,
          -1,  1,  8,  1, -1,
          -1,  1,  1,  1, -1,
          -1, -1, -1, -1, -1]

uart = UART(3, 9600, timeout_char=1000)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 1000)

clock = time.clock()

while(True):
    warning = False
    clock.tick()
    img = sensor.snapshot()
    img.morph(kernel_size, kernel)
    blobs = img.find_blobs([warning_threshold])
    if blobs:
        for b in blobs:
            img.draw_rectangle(b[0:4])
            img.draw_cross(b[5], b[6])
            #print(b[5], b[6])
            if b[6]>=160 and b[6]<=240 and b[5]<=280 and b[5]>=40:
                warning = True
                break
                pass
            pass
        pass
    if warning:
        uart.write('\xea\xfc\x22\xef')
        print('warning!')
    else:
        uart.write('\xea\xfc\x88\xef')
        print('ok!')

    print(clock.fps())
