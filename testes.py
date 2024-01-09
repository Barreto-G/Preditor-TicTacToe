import numpy as np

array = np.array([[-1,2,0],[2,0,-1],[3,-9,10]])
array1 = np.array([[-1,2,0],[2,0,-1],[3,-9,10]])
array2 = np.array([[5,1,0], [-4,0,5], [3,6,-8]])
array_resposta = (array == array2)
array_resposta2 = (array == array1)

print(array_resposta)
if False in array_resposta:
    print('Tem mentira')