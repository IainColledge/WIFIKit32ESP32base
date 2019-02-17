# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

from machine import I2C, Pin
import gc
import wifi_config
import ssd1306
import webrepl


def do_connect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)

    if not sta_if.isconnected():
        # Initialise the display
        pin16 = Pin(16, Pin.OUT)
        pin16.value(1)

        # Setup display variables
        i2c = I2C(scl=Pin(15), sda=Pin(4))
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)

        oled.fill(0)
        oled.text('Connecting to', 0, 0)
        oled.text('SSID: ' + wifi_config.ssid, 0, 10)
        oled.show()

        sta_if.active(True)
        sta_if.connect(wifi_config.ssid, wifi_config.password)
        ap_if.active(False)
        while not sta_if.isconnected():
            pass

        ip = network.WLAN(network.STA_IF).ifconfig()[0]

        oled.fill(0)
        oled.text('Connected to', 0, 0)
        oled.text('SSID: ' + wifi_config.ssid, 0, 10)
        oled.text('IP: ' + ip, 0, 20)
        oled.show()


do_connect()
webrepl.start()
gc.collect()
