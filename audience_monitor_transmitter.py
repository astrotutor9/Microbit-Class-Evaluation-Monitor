from microbit import *
import radio

radio.on()

# Start with no message sent out and no shaken responses
message_sent = False
shakes = 0

while True:
    # monitor for shaking
    # if a question has been asked send a message if shaken
    # display an image as proof of dispatch
    if accelerometer.was_gesture('shake') and message_sent == False:
        shakes += shakes + 1
        if shakes >= 3:
            radio.send("applause")
            message_sent = True
            display.show(Image.HAPPY)

    # the opposite of a happy shake response, no movement to register
    if accelerometer.was_gesture('face down'):
        message_sent = False
        shakes = 0
        display.clear()