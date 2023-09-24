# Program buttons to change the program state
def on_button_pressed_a():
    global state
    state = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global state
    state = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# In our forever loop we measure a sound, find the plot value,
# and find the value the motor should move to. Then we move the motor
# If the state is not 'ON' then we make the microbit sleep
# This time we reverse the direction of the motor!
def on_forever():
    global plot_value
    if state == 1:
        plot_value = Math.round(input.sound_level() / 131 * 180)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 180 - plot_value)
        led.plot_bar_graph(plot_value, 180)
        basic.pause(500)
    else:
        basic.show_icon(IconNames.ASLEEP)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 180)

# Here we start the program, initialise the variables, and start the forever loop
plot_value = 0
state = 0
basic.show_icon(IconNames.FABULOUS)
Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 180)
basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever)
