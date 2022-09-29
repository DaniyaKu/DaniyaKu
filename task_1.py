#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # импорт библиотеки (модуля)
import numpy # импорт библиотеки для создание массива
import matplotlib.pyplot as mpp # импорт библиотеки для создания графикав

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': # для того, чтобы обезопасить импорт модуля от нежелательных побочных эффектов
    arguments = numpy.arange(0, 200, 0.1) # задание промежутков
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # построение графика
    )
    mpp.show() # показ графика на экране
