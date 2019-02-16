# WIFI Kit 32 ESP32 Base

Base wifi connectivity, config and display [micropython](http://micropython.org/) code for the [WIFI Kit 32 ESP32 WIFI wireless with 0.96 inch OLED Display dev board](https://www.amazon.co.uk/gp/product/B078MCR8FY/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1).

To configure wifi settings create a file wifi_config.py such as:

````
#
# Wifi Config
#


ssid = "Your wifi name"
password = "Your wifi password"
````

Do not add to git and this allows for local config without sharing your secrets on Github.

#Notes

The ssd1306 built in library doesn't seem to be in the image for micropython 1.10, hence included here.
