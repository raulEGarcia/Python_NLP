
#PY FOR NLP - RAUL E GARCIA
#siliconvalleypro1@yahoo.com

import math
import numpy as np


def sigmoid(z): 
    ''' LIKE AN ON/OFF SWITCH CURVE

    Input:
        z: is the input (can be a scalar or an array)
    Output:
        h: the sigmoid of z
    '''
    
    
    ### START CODE ###
    # calculate the sigmoid of z
    
    if np.isscalar(z):
       h = 1/(1+math.exp(-z))
    else: 
       h = [ 1/(1+math.exp(-x)) for x in z ]

    ### END CODE HERE ###
    
    return h

# delete below - only verifications - easy to get OVERFLOWS EXP - RUN TIME ERROR

if (sigmoid(0) == 0.5):
    print('OK - FOR 0 WE HAVE .5')
else:
    print('ERROR')


def test1():
   print("X=0: ",sigmoid(0))
test1()

def test2():
   print("X=1: ",sigmoid(1))
test2()

def test3():
   print("X=-1: ",sigmoid(-1))
test3()

def test4():
   print("X=[0,1,-1]: ",sigmoid([0,1,-1]))
test4()



#
#def test5():
#   print(sigmoid([-1000,-1,0,1,1000])) #- OVERFLOW
#test5()
   

def test6():
   print("X=[-10,-1,0,1,10]: ",sigmoid([-10,-1,0,1,10]))
test6()
   