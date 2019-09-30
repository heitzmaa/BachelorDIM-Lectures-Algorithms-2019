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

"""---------------------------------------------------"""

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
"""--------------------------------------------------"""

"""fonction qui va calculer la moyenne d'un tableau rentré"""

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

"""-------------------------------------------------"""

"""fonction pour retourner la valeur max du tableau
on va définir une valeur max a zéro et elle va prendre
la valeur changera lorsqu'une valeur plus grande sera
trouvée dans le tableau
 et qui va retourner l'index"""

def max_value(table):
 #  return max(table)
   maxi=0

   for i in range(len(table)): 
       if table[i] >maxi:
           maxi = table[i]
         
   return(maxi, i)


print('valeur max et son index:',max_value(tableau))

"""-------------------------------------------------"""

"""fonction qui va inverser le tableau

Args: a list of values
return : reversed table
print(tableau[::-1])
print(tableau.reverse())"""

def reverse_in_place(table):     
    size = len(table)            
    index = size - 1
    its = size//2    # int(size/2)            
    for i in range(its):    
        temp = table[index]    
        table[index] = table[i]
        table[i] = temp
        index -= 1
    return(table)

print('tableau inversé:',reverse_in_place(tableau))


"""------------------------------------------------"""

#import numpy as np
import cv2

    #def roi_bbox(input_image : numpy array)
   
matrix=np.zeros((10,10),dtype=np.int32)

matrix[3:6, 4:8]=np.ones((3,4),dtype=np.int32)

for idrow in range(matrix.shape[0]):
    for idcol in range (matrix.shape[1]):
        pixVal=matrix[idrow,idcol]
"""
img=cv2.imread('img.png',0)
cv2.imshow('read image',img)
cv2.waitKey()
"""
 #cv2.boundingRect(cnt) for x, y 

"""       top= H
        bottom=0
        left=
        right=
        
        for col in range(L):
            for row in range(H):
                if mat[row,col]==1:
                    
                    if top == -1:
                        top = row
                        break
                    
                    if top!=-1:
                        break
                    --------------------
                
                    if top > row:
                        top=row
                    
                    if bottom < row:
                        bottom = row
                
                    if left < col:
                        left=col
                    
                    if right > col:
                        right = col
                   """




