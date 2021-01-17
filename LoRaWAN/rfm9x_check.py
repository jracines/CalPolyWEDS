"""
Wiring Check, Pi Radio w/RFM9x

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_ssd1306
import adafruit_rfm9x

RADIO_FREQ_MHZ = 868.0

def main():
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
        send = 'n'
        send = input("Send data (y/n)???? ")
        if (send == 'y'):
           packet_text = input("Enter data: ")
           packet_text = bytes(packet_text, "utf-8")
           rfm9x.send(packet_text)
        else: 
            while True:
                packet = rfm9x.receive()
                if packet is None:
                    print("- Waiting for PKT")
                else:   
                    # Process and print packet
                    prev_packet = packet
                    packet_text = str(prev_packet, "utf-8")
                    print("RX: "+packet_text)

                    # Send a reply
                    prev_packet = "Stop it please\r\n"
                    packet_text = bytes(prev_packet, "utf-8")
                    print("TX: "+prev_packet)
                    rfm9x.send(packet_text)

                    time.sleep(1)
                time.sleep(0.1)

if __name__ == "__main__":
    main()
