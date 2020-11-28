#!/usr/bin/python3

""" DIYHA Alarm Controller:
    Manage a simple digital high or low GPIO pin.
"""

# The MIT License (MIT)
#
# Copyright (c) 2020 parttimehacker@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import digitalio


class AlarmController:
    """ Abstract and manage an alarm GPIO pin. """

    def __init__(self, pin):
        """ Initialize the alarm GPIO pin. """
        self.gpio = digitalio.DigitalInOut(pin)
        self.gpio.direction = digitalio.Direction.OUTPUT
        self.gpio.value = True

    def sound_alarm(self, turn_on):
        """ Turn on or off power to the GPIO pin. """
        """ Pull down to activate the relay """
        if turn_on:
            self.gpio.value = False
        else:
            self.gpio.value = True

    def reset(self, ):
        """ Turn power off to the GPIO pin. """
        self.gpio.value = True
