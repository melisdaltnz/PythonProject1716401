# PythonProject/1716401/MelisAltınöz
Welcome to MelCulator! 
Description: In that program you can find the mean values, variance and min-max values of your datasets and draw a plot. You can enter your own dataset or you can choose a file. Also you can make unit conversion.

How to Run:
Program has 9 functions. 
1. function: If user has a data file, datas can be uploaded to the code by writing file directory and file name.
2. function: If user wants to use another a data file from same directory, it can be uploaded by using this function. 
3. funtion: Data can be checked by validation of data.
4. function: Unit conversion of the entered number is made between the following units.
    1.g to kg
    2.F to C
    3.cm to m
    4.kg to g
    5.C to K
    6.m to cm
5. function: Calculates the mean value of the uploaded data or a new array can be generated.
6. function: Calculates the variance of the uploaded data or a new array can be generated.
7. function: Calculates the maximum value of the uploaded data or a new array can be generated.
8. function: Calculates the minimum value of the uploaded data or a new array can be generated.
9. function: Normal or scattered plot is drawned by using random dataset or a new array can be generated.

Requirements:
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    import random
