#From ukbaz.github.io/howto/ubit_workshop.html

import time
from bluezero import microbit
from sense_hat import SenseHat
from picamera import PiCamera

sense = SenseHat()

ubit = microbit.Microbit(adapter_addr='B8:27:EB:0B:AA:BE',
                         device_addr='E6:51:A6:1A:37:5B',
                         accelerometer_service=True,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=True)

looping = True

#Microbit display arrays
mbX = [
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b10001]

#Currently used as Bluetooth connected icon
mbHappyFace = [
    0b00000,
    0b01010,
    0b00000,
    0b10001,
    0b01110]

#Currently used as Bluetooth disconnected icon
mbSadFace = [
    0b00000,
    0b01010,
    0b00000,
    0b01110,
    0b10001]

mbBellLeft = [
    0b00100,
    0b01100,
    0b11100,
    0b01100,
    0b10100]

mbBellCentre = [
    0b00100,
    0b01110,
    0b01110,
    0b11111,
    0b00100]

mbBellRight = [
    0b00100,
    0b01110,
    0b00111,
    0b00110,
    0b00101]

#Sense HAT display arrays
B = [0,0,255]  #Blue - use this for Bluetooth related stuff
N = [0,0,0]    #Off

#Currently used as Bluetooth connected icon
piHappyFace = [
N,N,N,N,N,N,N,N,
N,B,B,N,N,B,B,N,
N,B,B,N,N,B,B,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,B,N,N,N,N,B,N,
N,N,B,B,B,B,N,N,
N,N,N,N,N,N,N,N
]

#Currently used as Bluetooth disconnected icon
piSadFace = [
N,N,N,N,N,N,N,N,
N,B,B,N,N,B,B,N,
N,B,B,N,N,B,B,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,B,B,B,B,N,N,
N,B,N,N,N,N,B,N,
N,N,N,N,N,N,N,N
]

sense.set_pixels(piSadFace)
ubit.connect()
sense.set_pixels(piHappyFace)
print('Connected... Press a button to select mode')

mode = 0
while looping:
    if ubit.button_a > 0 and ubit.button_b > 0:
        mode = 3
        ubit.pixels = mbX
        time.sleep(1)
    elif ubit.button_b > 0:
        mode = 2
        ubit.pixels = mbSadFace
        sense.set_pixels(piSadFace)
        time.sleep(1)
    elif ubit.button_a > 0:
        mode = 1
        ubit.pixels = mbHappyFace
        sense.set_pixels(piHappyFace)
        time.sleep(1)

    if mode == 1:
        x, y, z = ubit.accelerometer
        if z < 0:
            print('Face up')
        else:
            print('Face down')
        time.sleep(0.5)
    elif mode == 2:
        print('Temperature:', ubit.temperature)
        time.sleep(0.5)
    elif mode == 3:
        looping = False
        print('Exiting')

ubit.disconnect()
sense.clear()