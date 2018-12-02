# Untitled - By: wmy - 周日 12月 2 2018

import sensor, image, time

warning_threshold   = (   20,   100,  -50,   50,   -55,   60)

kernel_size = 1
kernel = [-1, -1, -1,
          -1, +8, -1,
          -1, -1, -1]

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
            if b[6]>=200 and b[5]<=300 and b[5]>=20:
                warning = True
                pass
            pass
        pass
    if warning:
        print('warning!')
    else:
        print('ok!')



    #print(clock.fps())
