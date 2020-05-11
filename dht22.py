#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

pin = 4  #GPIO4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    #print = (temperature)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    mytemp = '{0:0.1f}'.format(temperature, humidity)
    myhum = '{1:0.1f}'.format(temperature, humidity)
    temp_output = open('/home/pi/iot/temp_data.txt', 'w')
    hum_output = open('/home/pi/iot/hum_data.txt', 'w')

    temp_output.write(mytemp)
    hum_output.write(myhum)

    temp_output.close
    hum_output.close

else:

    print('Failed to get reading. Try again!')
