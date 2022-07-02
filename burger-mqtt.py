# burgerbot with wifi
# Kevin McAleer
# July 2022

from burgerbot import Burgerbot
from secret import ssid, password
from umqttsimply import MQTTClient
from machine import Pin
import network
from time import sleep

mqtt_broker = "192.168.1.152"
client_id = "burgerbot"
left_motor_topic = "robot/burgerbot/left_motor"
right_motor_topic = "robot/burgerbot/right_motor"

# Setup the Wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# MOTOR_1 = Pin(6, Pin.OUT)
# MOTOR_2 = Pin(26, Pin.OUT)
# MOTOR_1_SPEED = Pin(7, Pin.OUT)
# MOTOR_2_SPEED = Pin(27, Pin.OUT)

bot = Burgerbot()

def sub_cb(topic, msg):
#     global MOTOR_1, MOTOR_2, MOTOR_1_SPEED, MOTOR_2_SPEED
    global bot
    
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    """ Subscribe call back """
    print(f'topic {topic}, msg {msg}')
    if topic == left_motor_topic:
        print(f"move left {float(msg)}")
#         MOTOR_1_SPEED = float(msg)
#         MOTOR_1 = 1
        bot.left_motor(float(msg))
    if topic == right_motor_topic:
        print(f"move right {float(msg)}")
#         MOTOR_2_SPEED = float(msg)
#         MOTOR_2 = 1
        bot.right_motor(float(msg))
                       

def connect_and_subscribe():
    """ Connect to the MQTT broker and subscribe to the topic"""
    global client_id, mqtt_broker
    
    
    print(client_id, mqtt_broker, left_motor_topic, right_motor_topic)
    client = MQTTClient(client_id, mqtt_broker, keepalive=30)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(left_motor_topic)
    client.subscribe(right_motor_topic)
    
    return client

def restart_reconnect():
    global client
    print('Failed to connect to MQTT broker, Reconnecting...')
    sleep(10)
    client = connect_and_subscribe()
    
# Connect to wifi
print("Connecting to Wifi...")
while wlan.isconnected() == False:
    pass
    
print("Connected")
print(wlan.ifconfig())

try:
    client = connect_and_subscribe()
except OSError as e:
    client = None
    restart_reconnect()

while True:
    try:
        client.check_msg()
            
    except OSError as e:
        restart_reconnect()