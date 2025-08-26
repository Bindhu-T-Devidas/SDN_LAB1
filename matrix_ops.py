import numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def transpose(A):
    return np.transpose(A)

if __name__ == "__main__":
    A = np.array([[1,2],[3,4]])
    B = np.array([[5,6],[7,8]])
    print("A + B =\n", add_matrices(A,B))
    print("Transpose of A =\n", transpose(A))
