'''
         Copyright (c) 2015 Sekou L. Remy
 
         Permission is hereby granted, free of charge, to any person obtaining a copy
         of this software and associated documentation files (the "Software"), to deal
         in the Software without restriction, including without limitation the rights
         to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
         copies of the Software, and to permit persons to whom the Software is
         furnished to do so, subject to the following conditions:
 
         The above copyright notice and this permission notice shall be included in
         all copies or substantial portions of the Software.
 
         THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
         IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
         FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
         AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
         LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
         OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
         THE SOFTWARE.

        Test program that turns and moves repeatedly.
'''

from time import sleep
from urllib2 import urlopen

temp_base_url = "http://somehost:someport/verb?";
permissions = "&id=somevalue";

def moveForward(velocity):
    twist = "&lx=%f" % velocity
    urlopen(temp_base_url+permissions+twist);

def turn(velocity):
    twist = "&az=%f" % velocity
    urlopen(temp_base_url+permissions+twist);


while 1:
    for loopCounter in range(5):
        turn(-9);
        sleep(1);

    for loopCounter in range(15):
        moveForward(-.1);
        sleep(1);
