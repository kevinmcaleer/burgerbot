# BurgerBot
BurgerBot is the Raspberry Pi Pico / Pico W powered round robot. 

This bite-sized robot uses the [Pimoroni Motor SHIM for Pico](https://www.pimoroni.com/motorshim) along with two Micro Metal Motors (N20 motors) with the JST connector attached. This makes connecting the Pico to the motors a piece of cake, or burger. 

BurgerBot also has a Range finder for detecting and avoiding objects (code comming soon).

---

## STL Files
You can download the STL files for this robot

- [`Base`](stl/base_v1.stl)
- [`Range Finder`](stl/rangefinder_v1.stl)
- [`Support`](stl/support_v1.stl)
- [`Top Section`](stl/topsection_v1.stl)
- [`Motor Holders`](stl/motor_holder_v6.stl)

---

## Code
You'll need to upload `umqttsimply.py` as well as `burgerbot.py` to the Pico/Pico W

### Working with Wifi
If you're using a Pico W you'll need to create a new python file on the Pico W named `secret.py` which contains two variables:

``` python
# secret.py
ssid = "your wifi name"
password = "your wifi password"
```
`burgerbot-mqtt.py` will read the secret.py when it is conencting to the Wifi network.