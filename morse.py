from gpiozero import LED, Button
from signal import pause
import time

#1. The length of a dot is one unit
#2. A dash is three units
#3. The space between parts of the same letter is one unit
#4. The space bewtween letters is three units
#5. The space between words is seven units 

led = LED(17)

def dot():
  led.on()
  time.sleep(.5)
  led.off()
  time.sleep(.5)

def dash():
  led.on()
  time.sleep(1.5)
  led.off()
  time.sleep(.5)

def letter_space():
    print('space between letter')
    led.off()
    time.sleep(1)

def word_space():
    print('word space')
    led.off()
    time.sleep(3)

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
    dash()
    dot()
    dot()

def letter_e():
    dot()

def letter_f():
    dot()
    dot()
    dash()
    dot()

def letter_g():
    dash()
    dash()
    dot()

def letter_h():
    dot()
    dot()
    dot()
    dot()

def letter_i():
    dot()
    dot()

def letter_j():
    dot()
    dash()
    dash()
    dash()

def letter_k():
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
    dash()
    dash()

def letter_n():
    dash()
    dot()

def letter_o():
    print("o")
    dash()
    dash()
    dash()

def letter_p():
    dot()
    dash()
    dash()
    dot()

def letter_q():
    dash()
    dash()
    dot()
    dash()

def letter_r():
    dot()
    dash()
    dot()

def letter_s():
    print("s")
    dot()
    dot()
    dot()

def letter_t():
    dash()

def letter_u():
    dot()
    dot()
    dash()

def letter_v():
    dot()
    dot()
    dot()
    dash()

def letter_w():
    dot()
    dash()
    dash()

def letter_x():
    dash()
    dot()
    dot()
    dash()

def letter_y():
    dash()
    dot()
    dash()
    dash()

def letter_z():
    dash()
    dash()
    dot()
    dot()