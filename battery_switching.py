import time;
#ADC setup:
import board;
import busio;
i2c = busio.I2C(board.SCL, board.SDA);
import adafruit_ads1x15.ads1115 as ADS;
from adafruit_ads1x15.analog_in import AnalogIn;
ads = ADS.ADS1115(i2c);
#output GPIO setup (battery swithing):
import RPi.GPIO as GPIO;
GPIO.setmode(GPIO.BCM);
GPIO.setwarnings(False);
GPIO.setup(5,GPIO.OUT);  #ctrl for battery1
GPIO.setup(6,GPIO.OUT);  #ctrl for battery2
GPIO.setup(13,GPIO.OUT); #ctrl for battery3
GPIO.setup(19,GPIO.OUT); #ctrl for battery4


chan0 = AnalogIn(ads, ADS.P0); #channel0 will read the voltage from the smoke detector
chan1 = AnalogIn(ads, ADS.P1); #channel1 will read the out+ battery voltage for battery switching
battery = 1; #denotes which battery is powering the device

#intital state: battery1 is powering
GPIO.output(5, GPIO.HIGH);
GPIO.output(6, GPIO.LOW);
GPIO.output(13, GPIO.LOW);
GPIO.output(14, GPIO.LOW);

while True:
    if (chan1.voltage < 2.5):
        if (battery == 4):
            battery = 1;
        else:
            battery += 1;
            
        if (battery == 1)
            GPIO.output(5, GPIO.HIGH);
            GPIO.output(6, GPIO.LOW);
            GPIO.output(13, GPIO.LOW);
            GPIO.output(14, GPIO.LOW);
        elif (battery == 2):
            GPIO.output(5, GPIO.LOW);
            GPIO.output(6, GPIO.HIGH);
            GPIO.output(13, GPIO.LOW);
            GPIO.output(14, GPIO.LOW);
        elif (battery == 3):
            GPIO.output(5, GPIO.LOW);
            GPIO.output(6, GPIO.LOW);
            GPIO.output(13, GPIO.HIGH);
            GPIO.output(14, GPIO.LOW);
        elif (battery == 4):
            GPIO.output(5, GPIO.LOW);
            GPIO.output(6, GPIO.LOW);
            GPIO.output(13, GPIO.LOW);
            GPIO.output(14, GPIO.HIGH);
    else:
    print("Battery Voltage:",round(chan1.voltage,3));
    time.sleep(3);



