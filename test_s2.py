#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: heitzmaa
"""
import S1_algotools as algo
import pytest


def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
"""--------------------------------------"""

def test_average_above_zero_V1():
   tableau=[0,3,5]
   test=algo.average_above_zero(tableau)
   assert test==4
   
def test_average_above_zero_V2():
   tableau=[0,-3,5]
   test=algo.average_above_zero(tableau)
   assert test ==5

def test_average_above_zero_V3():
   with pytest.raises(ZeroDivisionError):
        tableau=[-8,-3,-5]
        algo.average_above_zero(tableau)
      
def test_average_above_zero_V4():
   with pytest.raises("average_above_zero, expected a list as input"):
        tableau=[]
        algo.average_above_zero(tableau)
        
"""------------------------------------ """