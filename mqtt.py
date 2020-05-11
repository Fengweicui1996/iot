#!/usr/bin/python
#encoding:utf-8

import paho.mqtt.client as mqtt
import random
import time
import json
import RPi.GPIO as GPIO

GPIO_PIN = 17
GPIO_PIN2 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN,GPIO.LOW)
GPIO.setup(GPIO_PIN2, GPIO.OUT)
GPIO.output(GPIO_PIN2,GPIO.LOW)
#链接
def on_connect( client , userdata,flags,rc ):
	print(str(re))
	pass

#发送消息回调函数
def on_message( elient, userdata , msg):
	s= msg.payload.decode("UTF-8")
	print(s)
	if s=="on":
		GPIO.output(GPIO_PIN,GPIO.HIGH)
	elif s=="off":
		GPIO.output(GPIO_PIN,GPIO.LOW)
	elif s=="1":
                GPIO.output(GPIO_PIN2,GPIO.HIGH)
	elif s=="0":
		GPIO.output(GPIO_PIN2,GPIO.LOW)

#设置网络参数
product_id="******" #产品ID
device_auth="******"  #鉴权key
device_id="*********" #设备ID
ip="183.230.40.39"
port=6002
client=mqtt.Client(client_id=device_id)
client.username_pw_set(product_id,device_auth)
client.on_connect=on_connect
client.on_message=on_message
client.connect(ip, port, 60)
client.loop_forever()

