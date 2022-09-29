# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:26:02 2022

@author: Elita
"""


# Program menghitung jarak antara dua titik di permukaan bumi menggunakan rumus dan fungsi trigonometri

import math
input("Masukan Nama Tempat P = ")
x1 = float(input("Masukan Latitude tempat P = "))
y1 = float(input("Masukan longitude tempat P = "))

print("======================================")

input("Masukan Nama Tempat Q = ")
x2= float(input("Masukan Latitude Tempat Q = "))
y2= float(input("Masukan longitude Tempat Q = "))

xlat = x2-x1
ylon = y2-y1

p = math.sin(math.radians(xlat/2)) **2 + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.sin(math.radians(ylon/2)) **2

# versi arc sinus
q = 2 * math.asin(math.sqrt(p))

# versi tangen 2
r = 6371.01

print("======================================")

print("jarak antara dua tempat adalah" , p*q , "kilometer")

print("======================================")


print("Programmer: Elita Wahyu Firdasari")
print("NIM: 065002200038")
print("Program Studi: Sistem Informasi")