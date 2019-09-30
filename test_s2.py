#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: heitzmaa
"""
import S1_algotools as algo
import pytest

"""
def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
"""

def test_average_above_zero_V1():
   tableau=[0,3,5]
   assert   algo.average_above_zero(tableau)==4
   
def test_average_above_zero_V2():
   tableau=[0,-3,5]
   test, lastID=algo.average_above_zero(tableau)
   assert test ==4

"""  
def test_average_above_zero_V3():
   tableau=[0,-3,5]
   test, lastID=algo.average_above_zero(tableau)
   assert test ==4"""