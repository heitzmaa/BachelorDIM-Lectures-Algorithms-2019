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
   with pytest.raises(ValueError):
        tableau=[]
        algo.average_above_zero(tableau)
  
def test_average_above_zero_V5():
   with pytest.raises(ValueError):
        tableau=["ee","d","n"]
        algo.average_above_zero(tableau)
        
"""------------------------------------ """
def test_max_value_V1():
    tableau=[0,5,4]
    test=algo.max_value(tableau)
    assert test== (5,2)
    
"""------------------------------------"""  
def test_reverse_in_place_V1(): 
    tableau=[0,5,4]
    test=algo.reverse_in_place(tableau)
    assert test== [4,5,0]


