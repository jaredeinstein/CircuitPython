import time

from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy
 
allowReset = 1 #set to 0 to disable user reset with the power button once started
                #if set to 0, wait until end of game, turn off all toggles, then turn off power
 
# Password combo variables
PASSWORD = [2,1,4,3]      #stores the password set
inputCode = [0,0,0,0]      #stores the input code set
entered = 0               #indicates a full code set has been entered
over = 0                  #state of game for escaping while loop
blinker = 0               #for decimal point blinking in updateDisplay function
 
# Switch variables
WHITESWITCHPIN =  "A1"   
REDSWITCHPIN =    "A3"
YELLOWSWITCHPIN = "A4"
BLUESWITCHPIN =  "A6"
 
whiteSwitchState =  0 #variable to read switch state, off/0 or on/1
redSwitchState =    0
yellowSwitchState = 0
blueSwitchState =   0
 
whiteSwitchPriorState =  0 #variable to store switch last state
redSwitchPriorState =    0
yellowSwitchPriorState = 0
blueSwitchPriorState =   0

pixelMaxBrightness = 0.04
 
fail = 0        # if fail != 0, the combination failed
success = 0     # counter for successfull entry of combination
count = 0       # number of switches flipped
 
 
# thousand millis per second
gTimer = 0
NORMAL = 1000
FAST = 30  #100 this is the rate for fast countdown when combo fails, smaller is faster
gDuration = "NORMAL"

setup = 0

while True:
    
    if not setup:
        if allowReset == 0:
            allowReset = 0
            #pinMode(A5, OUTPUT);  #disables the on/off button
            #digitalWrite(A5, LOW);  #disables the on/off button
        
        gTimer = 180

        cpx.red_led = True

        cpx.pixels.brightness = 0

        cpx.pixels[6] = (255, 255, 255)
        cpx.pixels[8] = (255, 0, 0)
        cpx.pixels[1] = (255, 255, 0)
        cpx.pixels[3] = (0, 0, 255)

        for i in range(5):
            cpx.stop_tone()
            cpx.start_tone(200 + (i*25))
            cpx.pixels.brightness = (pixelMaxBrightness * (i/5))
            time.sleep(.20)
        cpx.stop_tone()
        setup = 1

    if cpx.touch_A1 and whiteSwitchPriorState == 0:
        inputCode[count] = 1
        count += 1
        whiteSwitchPriorState = 1
        print ("touched white A1, count is")
        print (count)
        print (inputCode)
        cpx.pixels[6] = (0,0,0)

    if cpx.touch_A3 and redSwitchPriorState == 0:
        inputCode[count] = 2
        count += 1
        redSwitchPriorState = 1
        print ("touched red A1, count is")
        print (count)
        print (inputCode)
        cpx.pixels[8] = (0,0,0)

    if cpx.touch_A4 and yellowSwitchPriorState == 0:
        inputCode[count] = 3
        count += 1
        yellowSwitchPriorState = 1
        print ("touched yellow A1, count is")
        print (count)
        print (inputCode)
        cpx.pixels[1] = (0,0,0)

    if cpx.touch_A6 and blueSwitchPriorState == 0:
        inputCode[count] = 4
        count += 1
        blueSwitchPriorState = 1
        print ("touched blue A1, count is")
        print (count)
        print (inputCode)
        cpx.pixels[3] = (0,0,0)

    if count == 4:
        entered = 1

    while entered != 0 and over == 0:
        if(inputCode[0]==PASSWORD[0] and inputCode[1]==PASSWORD[1] and inputCode[2]==PASSWORD[2] and inputCode[3]==PASSWORD[3]):
            success = 1
            over = 1
        else:
            fail = 1
            over = 1
            print ("failed")
            gDuration = "FAST"
    
    while success == 1:
        cpx.pixels.fill((0,255,0))

    while fail ==1:
        cpx.pixels.fill((255,0,0))
