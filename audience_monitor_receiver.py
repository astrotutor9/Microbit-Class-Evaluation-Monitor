from microbit import *
import random
import radio

radio.on()

# responses received start at zero
responses = 0

while True:
    # listen for responses from class
    message = radio.receive()

    # count the responses received
    if message:
        responses += 1

    # if A open file, ammend with number of responses
    # once class has sent all their responses
    if button_a.was_pressed():
        with open('numbers.txt', 'r') as my_file:
            content = my_file.read()

        with open('numbers.txt', 'w') as my_file:
            detail = content + str(responses) + ","
            my_file.write(detail)

        # show number of responses and reset variable for next question
        display.scroll(responses)
        responses = 0
        sleep(500)
        display.clear()

    # to reset the file record hold the Microbit facedown
    # without needing to turn off Microbit
    if accelerometer.was_gesture('face down'):
        with open('numbers.txt', 'w') as my_file:
            my_file.write("")
        # wipes file information
        sleep(250)

    # if B read back the contents of the file to record the results
    # the file is lost once Microbit is powered off
    if button_b.was_pressed():
        with open('numbers.txt', 'r') as my_file:
            content = my_file.read()
        # display file contents
        display.scroll(content)
        sleep(250)