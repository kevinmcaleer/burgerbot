# Function Reference

**BurgerBot** uses the [Pimoroni Motor SHIM for Pico](https://www.pimoroni.com/motorshim) and the Pimoroni Micropython build that goes along with it. 

The Pimoroni MicroPython firmware has '*batteries included*' libraries for all their products, and is therefore slightly different than standard MicroPython. If you get any error message about the `motor` library not being found, you now know why.

# Burgerbot Class

## Properties
### `speed`
Speed is an overall speed value for the motors, and is between `-1` (reverse), `0` (stationary), and `1` (full forward). To set the motor speed to `50%`, simply set the speed value to `0.5`:

```python
# Create a Burgerbot instance
mac = Burgerbot()

# Set the speed to 50%
mac.speed = 0.5
```

## Methods
### `forward`
Drives both motors forward at the currently set speed.

```python
# Move forward
mac.forward()
```

### `backward`
Drives both motors backward at the currently set speed.

```python
# Move backward
mac.backward()
```

### `turn_left`
Turns the robot left by driving the motors in opposite directions.

```python
# Turn left
mac.turn_left()
```

### `turn_right`
Turns the robot right by driving the motors in opposite directions.

```python
# Turn right
mac.turn_right()
```

### `stop`
Stops both motors immediately by disabling them.

```python
# Stop the motors
mac.stop()
```

## BurgerBot V2
### `pen_up`
Moves the pen servo to the up position (e.g., for lifting the pen off the surface).

```python
# Lift the pen
mac.pen_up()
```

### `pen_down`
Moves the pen servo to the down position (e.g., for drawing on the surface).

```python
# Lower the pen
mac.pen_down()
```

### `pen_middle`
Moves the pen servo to the middle position, typically used for calibration.

```python
# Move pen to the middle position
mac.pen_middle()
```
