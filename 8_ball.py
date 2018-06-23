import time
import random
import os

def ball():
    image_choices = ['absolutely.jpg', 'ask-agin.jpg', 'cannot-tell-now.jpg', 'count-on-it.jpg', 'go-for-it.jpg', 'it-is-ok.jpg', 'it-will-pass.jpg', 'maybe.jpg', 'no-doubt.jpg', 'no.jpg', 'not-now.jpg', 'very-likely.jpg', 'wait-for-it.jpg', 'yes.jpg', 'youre-hot.jpg']
    choice = random.randint(0,14)
    command = 'sudo /var/lib/cloud9/8_ball/display.sh ' + image_choices[choice]
    print(choice)
    print(command)
    os.system(command)
    time.sleep(5)

while True:
    time.sleep(0.1)
    f_angvel_x = open("/sys/bus/i2c/devices/2-0069/iio:device1/in_anglvel_x_raw", "r")
    x_anglvel = int(f_angvel_x.read())
    f_angvel_y = open("/sys/bus/i2c/devices/2-0069/iio:device1/in_anglvel_y_raw", "r")
    y_anglvel = int(f_angvel_y.read())
    f_angvel_z = open("/sys/bus/i2c/devices/2-0069/iio:device1/in_anglvel_z_raw", "r")
    z_anglvel = int(f_angvel_z.read())
    if abs(x_anglvel) > 1000 and abs(y_anglvel) > 1000 and abs(z_anglvel) > 1000:
        ball()
    f_angvel_x.close()


