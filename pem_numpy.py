import numpy as np 
import time 

#Tests sur les arrays
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.empty([2])
c = np.concatenate((a[0],a[1]))
x = np.array([[1, 2], [3, 512]])
y = np.array([[5, 6]])
z = np.concatenate((x, y))
z = np.reshape(z,newshape=(2,3)) 
#print("hello world")
#print(z)

def tab_complex(N):
    """ renvoie un tableau Numpy de taille NxN, dont les éléments sont de type np.complex, et tel que si A= tab_complexe(N) alors A[x,y] est  x+iy, où ici  i2=−1"""
    tab = np.zeros(shape= (N,N), dtype= np.complex64)
    I=1j
    for x in range(N):
        for y in range(N):
            tab[x,y] = x + y*I
    return tab

a = time.time()
tab_complex(10000)
print("Temps pour la fonction 1 : ", time.time()-a)

def tab_complex_v2(N):
    """meme fonction mais plus rapide"""
    tab =  np.arange(10,dtype=np.complex64)
    tab = np.stack([tab]*10,axis=1)
    I=1j
    for x in range(np.ravel(tab).size):
        np.ravel(tab)[x] = x//10+ x%10*I 
    return tab
    
b = time.time()
tab_complex_v2(10000)
print("Temps pour la fonction 2 : ", time.time()-b)



