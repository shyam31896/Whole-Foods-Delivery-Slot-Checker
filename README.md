# Whole Foods Delivery Slot Checker

This repository consists of an automated script which identifies the available Delivery slots from Amazon Whole Foods in this time of heavy demand for grocies during the COVID-19 pandemic. This script supports Google Chrome and Mozilla Firefox Web browsers and notifies about the delivery slots (if available) through E-mail. The script will guide you through the required information necessary for the processing, and be sure to look into the Usage examples provided below.

## Supporting Platforms:

Tested on *Linux* and *Windows*. Ongoing Testing for *MacOS*. Releasing soon.

## Supported Browsers:

Tested on *Google Chrome* and *Mozilla Firefox*. (Please install the proper versions of `chromedriver` and `geckodriver` respectively for Chrome and Firefox for proper functioning. Don't fret, the program will guide you!)

## Usage:

```sh
$ python3 checker_cf_supported.py -b [ Chrome/Firefox ]
```

Nothing complicated. Just execute the above mentioned command and follow the instructions and Voila! 

You will need to login once into your Amazon account and proceed until you reach the page where you will choose the delivery slots. Terminate the program and restart it for the program to check for the availability of delivery slots.

## Powered By:

<p align="center">
  <a href="https://www.selenium.dev/" target="_blank"><img width="55" height="60" src="https://www.selenium.dev/images/selenium_logo_square_red.png"></a>
</p>