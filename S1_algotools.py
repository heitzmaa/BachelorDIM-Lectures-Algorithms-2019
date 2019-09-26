# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:16:56 2019

@author: heitzmaa
"""

print('My first Python3 trials')

myVariable=0
print('MyVariable=',myVariable)

''' 
question 1 : 
   si somme pas init: le calcul de fin va être faux car 
   il va mettre n import quelle valeur genre aléatoire
'''

''' 
question 2 : 
   si les valeurs sont négatives : 
   il va faire une division par 0 car dans la condition
   les nombres doivent être sup à 0
'''

import numpy as np

tab_list=[1,2,3-4,5,-9]
tab_zeros=np.zeros(12,dtype=np.int32)
tab_fromList=np.array(tab_list)

for id in range (len(tab_fromList)):
    print('tab['+str(id)+'='+str(tab_fromList[id]))
    print('tab[{index}]=(val)'.format(index=id,val=tab_fromList[id]))
    
    if tab_fromList[id] >0:
        print('youpi')
        
print('finished')

"""--------------------------------------------------------"""

def mySum(param1, param2):
    
    """
    function that sum the two input params
    Args:
        param1: an int value
        param2: an int value
    returns the sum
        
    """
    return param1+param2

print('sum Test:',mySum(3,4))


#fonction qui va calculer la moyenne d'un tableau rentré

def average_above_zero(table):
   Som=0
   N=0

   for i in range(len(table)): 
       if table[i] >0:
           Som = Som + table[i]
           N= N+1
   Moy = Som/ N
   return Moy
   

tableau=[0,5,10] 
print('moyenne:',average_above_zero(tableau))
