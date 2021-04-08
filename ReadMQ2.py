import time;
#ADC setup:
import board;
import busio;
i2c = busio.I2C(board.SCL, board.SDA);
import adafruit_ads1x15.ads1115 as ADS;
from adafruit_ads1x15.analog_in import AnalogIn;
ads = ADS.ADS1115(i2c);

chan0 = AnalogIn(ads, ADS.P0); #channel0 will read the voltage from the smoke detector

while True:
    volts = chan0.voltage;
    RS_gas = (5-volts)/volts;
    #R0 = RS_air/9.8;
    R0 = .385;
    ratio = RS_gas/R0;
    print("Smoke Voltage",round(volts,3));
    print("ratio", round(ratio,3));
    time.sleep(3);