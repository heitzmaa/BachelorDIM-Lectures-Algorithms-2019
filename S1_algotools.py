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
    '''
    computes the average of positive values
    Args: a list of values
    returns: the average of positive values
    raise value error if input param is not a list
    '''
    
    if not(isinstance(table,list)):
        raise ValueError('average_above_zero, expected a list as input')
    if len(table)==0:
        raise ValueError('expected a non empty a list as input')
    if not(isinstance(table[0], (int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')
        
    
    Som=0
    N=0
        
    for i in range(len(table)): 
        if table[i] >0:
            Som = Som + table[i]
            N= N+1
    Moy = Som/ N
    return Moy
   

tableau=[0,3,5] 
print('moyenne:',average_above_zero(tableau))


#fonction pour retourner la valeur max du tableau
#on va définir une valeur max a zéro et elle va prendre
#la valeur changera lorsqu'une valeur plus grande sera
#trouvée dans le tableau
# et qui va retourner l'index

def max_value(table):
 #  return max(table)
   maxi=0

   for i in range(len(table)): 
       if table[i] >maxi:
           maxi = table[i]
         
   return(maxi, i)


print('valeur max et son index:',max_value(tableau))


#fonction qui va inverser le tableau
#reverse_a = a[::-1]
'''
def reverse_table(table):

   maxi=0

   for i in range(len(table)): 
       if table[i] >maxi:
           maxi = table[i]
         
   return maxi


print('tableau inversé:',reverse_table(tableau))
'''



