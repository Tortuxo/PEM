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

def tab_complex_v2(N):
    """meme fonction mais plus rapide"""
    tab =  np.arange(N,dtype=np.complex64)
    im = np.stack([tab]*N)
    tab = np.stack([tab]*N,axis=1)
    return tab +1j*im
    
#Tests de concatenation
a = np.arange(8, dtype=np.complex64)
b = np.arange(8)
b = b*1j
#print(b)
#print(a+b)
j = np.random.randint(-10,10,size=(5,8))


x[x<500]=np.array([11,1,13])

def f(A):
    """prend en paramètre un tableau Numpy A et qui renvoie un tableau B qui est une copie de A dans laquelle les nombres  <0
    ont été remplacés par  0
    et les nombres  >1
    ont été remplacés par  1"""
    B = A.copy()
    B[B<0]=0
    B[B>1]=1
    return B

