#!/usr/bin/env/python
"""evelandy/W.G.
Aug. 06 2018 10:38pm
Profanity Checker
Python36-32
to use, just type the extention and filename.ext
of the file you want to check when prompted. 
"""

import urllib.request
from urllib.parse import urlencode


filename = input("Enter the filename and extention of your file")

def read_txt():
    with open(filename) as file:
        doc = file.read()
    print(doc)
    profan_chk(doc)


def profan_chk(txt):
    rule = urlencode({' ' : txt})
    with urllib.request.urlopen("http://wdylike.appspot.com/?q="+rule) as site:
        results = site.read()
    print(results)

    if results == b'false':
        print("all good here!")
    else:
        print("check your text!!!")



read_txt()

