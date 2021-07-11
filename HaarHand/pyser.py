# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:14:04 2020

@author: sangmesh
"""

import serial
ser = serial.Serial('COM16', 9800, timeout=1)
ser.write(b'H')
# ser.write(b'L')
# ser.write(b'H')
# ser.write(b'L')
ser.close()
