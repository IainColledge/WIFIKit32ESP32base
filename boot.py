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
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi_config.config["ssid"], wifi_config.config["password"])
        ap_if.active(False)
        while not sta_if.isconnected():
            pass

    ip = network.WLAN(network.STA_IF).ifconfig()[0]

    pin16 = Pin(16, Pin.OUT)
    pin16.value(1)
    i2c = I2C(scl=Pin(15), sda=Pin(4))#
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    oled.fill(0)
    oled.text('SSID: ' + wifi_config.config["ssid"], 0, 0)
    oled.text('IP: ' + ip, 0, 10)
    oled.show()

do_connect()
webrepl.start()
gc.collect()