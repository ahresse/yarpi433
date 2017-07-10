import time
import sys
import RPi.GPIO as GPIO

sync_length = 0.00246
#53 bit long code
open_code = '0101010101010101010101010101010101010101010101010101'
pulse_length = 0.000410
attempt_delay = 0.01

NUM_ATTEMPTS = 4
TRANSMIT_PIN = 17

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    for t in range(NUM_ATTEMPTS):
        GPIO.output(TRANSMIT_PIN, 1)
        time.sleep(sync_length)
        for i in code:
            GPIO.output(TRANSMIT_PIN, 0)
            time.sleep(pulse_length)
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(pulse_length)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(pulse_length)
            else:
                continue
            GPIO.output(TRANSMIT_PIN, 1)
            time.sleep(pulse_length)
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(attempt_delay)

try:
    if __name__ == '__main__':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
        for argument in sys.argv[1:]:
            exec('transmit_code(' + str(argument) + ')')

except:
    print "Error"

finally:
    GPIO.cleanup()
