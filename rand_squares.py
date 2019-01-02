#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 19:11:39 2019

@author: orionis
"""

from PIL import Image
import random

im = Image.open('fill.jpg')

width, height = im.size


'''Start by taking an appropriate width and height for the starting point
then length is chosen as the entire width minus some value between the starting
point and the width, this gives us a length that is restricted by the width of the
image. 
Then we check if the length of the square exceeds the height of the image and 
change the length till this condition doesn't hold true'''
def decide_start_and_length():
    start_w, start_h = (random.randint(0, width), random.randint(0, height))
    length = width - random.randint(start_w, width)
    print("Length within:", length)
    while start_h + length > height:
        length = width - random.randint(start_w, width)
    return (start_w, start_h, length)
        
    
def random_square():
    start_w, start_h, length = decide_start_and_length()
    print("Width:", width, "Height:", height)
    print("Starting Point:", (start_w, start_h))
    print("Length of side:", length)
    for row in range(length):
        for col in range(length):
            im.putpixel((start_w + col, start_h + row), (0, 0, 90))
            #(col, row) are the coordinates. iterating throught the region of the 
            #square starting from the starting coordinates of the square
    im.save('squares.jpg')       
n_squares = int(input("How many squares? "))

for number in range(n_squares):
    random_square()