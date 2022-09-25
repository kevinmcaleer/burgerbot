# Function Reference

**BurgerBot** uses the [Pimoroni Motor SHIM for Pico](https://www.pimoroni.com/motorshim) and the Pimoroni Micropython build that goes along with it. 

The Pimoroni MicroPython firmware has '*batteries included*' libraries for all their products, and is therefore slightly different than standard MicroPython. If you get any error message about the `motor` library not being found, you now know why.

# Burgerbot class

## Properties
### `speed`
Speed is an overall speed value for the motors, and is between `-1` (reverse), `0` (stationary) and `1` - full forward.
To set the motor speed to `50%`, simply set the speed value to `0.5`:

``` python
# Create a Burgerbot
mac = Burgerbot()

# Set the speed to 50%
mac.speed = 0.5
```

## Methods
### `forward`
### `backward`
### `turnleft`
### `turnright`
### `stop`

## BurgerBot V2
### `Pen_up`
### `Pen_down`