import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5],[6]])
print("A=")
print(A)
print("B=")
print(B)
D = 2*A
print("2*A=")
print(D)
print("Transposee(A)=")
print(A.T)
print("C=A*B=")
C = np.dot(A,B)
print(C)
A_inv = np.linalg.inv(A)
print("A**-1=")
print(A_inv)
E = np.array([[3,1,1],[1,3,1],[1,1,3]])
print("E=")
print(E)
spectre,vecteur = np.linalg.eig(E)
print("Spectre =",spectre)
print("Vecteurs propres =")
print(vecteur)
