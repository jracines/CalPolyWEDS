#general setup
import time
import busio

#GPIO library
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LoRa setup
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_ssd1306
import adafruit_rfm9x

#ADC setup
i2c = busio.I2C(board.SCL, board.SDA);
import adafruit_ads1x15.ads1115 as ADS;
from adafruit_ads1x15.analog_in import AnalogIn;
ads = ADS.ADS1115(i2c);


RADIO_FREQ_MHZ = 868.0

def main():
    #GPIO pin 17(button) to be an input with pull up resistor
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.input(17)

    #setup pin 18 to be an output with pull down (used for LED)
    #GPIO.setup(18, GPIO.OUT)
    #GPIO.output(18,GPIO.LOW)
    
    # Configure RFM9x LoRa Radio
    # CS = DigitalInOut(board.CE1)
    CS = DigitalInOut(board.D7)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    # spi = busio.SPI(board.D11, MOSI=board.D10, MISO=board.D9)
    print("SPI ok!")
   
    try:
        # Attempt to set up the RFM9x Module
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
        print("RFM9x: Detected")
    except RuntimeError as error:
        # Thrown on version mismatch
        print('RFM9x Error: ', error)
        exit(-1)

    while True:
        send = 'n' #smoke sensor data packet will be sent when the button is pressed
        #debouce for when button is pressed
        if GPIO.input(17) == GPIO.LOW:
            time.sleep(.05)
            if GPIO.input(17) == GPIO.LOW:
                send = 'y'
        if (send == 'y'): #for sending a packet
           chan0 = AnalogIn(ads, ADS.P0); #channel0 will read the voltage from the smoke detector
           volts = chan0.voltage;
           RS_gas = (5-volts)/volts;
           #R0 = RS_air/9.8;
           R0 = .385; # measured value of R0
           ratio = RS_gas/R0;
           #print("Smoke Voltage:",round(volts,3));
           packet_text = "Ratio: " + str(round(ratio,3));
           packet_text = bytes(packet_text, "utf-8")
           rfm9x.send(packet_text)
           send = 'n'
        else: #for recieving a packet
            print("waiting")
            time.sleep(0.1)

if __name__ == "__main__":
    main()
