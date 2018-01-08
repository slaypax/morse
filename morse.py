from gpiozero import LED, Button
from signal import pause
import time
import morse_config as config

#1. The length of a dot is one unit
#2. A dash is three units
#3. The space between parts of the same letter is one unit
#4. The space bewtween letters is three units
#5. The space between words is seven units 

led = LED(config.settings['gpio_pin'])
unit = config.settings['unit']

def dot():
  led.on()
  time.sleep(unit)
  led.off()
  time.sleep(unit)

def dash():
  led.on()
  time.sleep(unit * 3)
  led.off()
  time.sleep(unit)

def letter_space():
    print('space between letter')
    led.off()
    time.sleep(unit * 3)

def word_space():
    print('word space')
    led.off()
    time.sleep(unit * 6)

def letter_a():
    print("a ")
    dot()
    dash()
    
def letter_b():
    print("b ")
    dash()
    dot()
    dot()
    dot()

def letter_c():
    print("c ")
    dash()
    dot()
    dash()
    dot()

def letter_d():
    print("d ")
    dash()
    dot()
    dot()

def letter_e():
    print("e ")
    dot()

def letter_f():
    print("f ")
    dot()
    dot()
    dash()
    dot()

def letter_g():
    print("g ")
    dash()
    dash()
    dot()

def letter_h():
    print("h ")
    dot()
    dot()
    dot()
    dot()

def letter_i():
    print("i ")
    dot()
    dot()

def letter_j():
    print("j ")
    dot()
    dash()
    dash()
    dash()

def letter_k():
    print("k ")
    dash()
    dot()
    dash()
    

def letter_l():
    print("l ")
    dot()
    dash()
    dot()
    dot()

def letter_m():
    print("m ")
    dash()
    dash()

def letter_n():
    print("n ")
    dash()
    dot()

def letter_o():
    print("o")
    dash()
    dash()
    dash()

def letter_p():
    print("p ")
    dot()
    dash()
    dash()
    dot()

def letter_q():
    print("q ")
    dash()
    dash()
    dot()
    dash()

def letter_r():
    print("r ")
    dot()
    dash()
    dot()

def letter_s():
    print("s")
    dot()
    dot()
    dot()

def letter_t():
    print("t ")
    dash()

def letter_u():
    print("u")
    dot()
    dot()
    dash()

def letter_v():
    print("v ")
    dot()
    dot()
    dot()
    dash()

def letter_w():
    print("w ")
    dot()
    dash()
    dash()

def letter_x():
    print("x ")
    dash()
    dot()
    dot()
    dash()

def letter_y():
    print("y ")
    dash()
    dot()
    dash()
    dash()

def letter_z():
    print("z ")
    dash()
    dash()
    dot()
    dot()