# Diff Pressure Click

Using a Raspberry Pi to read differential pressure
## Hardware
I went for the 2-way shield but there is a single shield availabe`
### Hardware used
* [pi2-shield](http://www.mikroe.com/click/pi2-shield/)
* [pressure click](http://www.mikroe.com/click/diff-pressure/)

I ordered mine from RS Components

### Alternative Hardware
* [Single pi shield](http://www.mikroe.com/click/pi-shield/)

### Install this software
From directory /home/pi issue command

**git clone https://github.com/KeithSloan/ClickDiffPressure.git**

## Setting up SPI
SPI must be enabled on the Raspberry Pi - 
Configuration
Run sudo raspi-config .
Use the down arrow to select 9 Advanced Options.
Arrow down to A7 I2C .
Select yes when it asks you to enable I2C.
Also select yes when it tasks about automatically loading the kernel module.
Use the right arrow to select the <Finish> button.
Select yes when it asks to reboot.
## Required Software libraries
Some programs use pigpio to install see (http://abyz.co.uk/rpi/pigpio/download.html)
LetterBoard needs festival text to speech

** sudo apt-get install festival

## Feedback

    Feedback to keith@sloan-home.co.uk



