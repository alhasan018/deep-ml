import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

  mat = np.array(a)
  vec = np.array(b)

  if mat.shape[1] == len(vec):
    dot_product = np.dot(mat,vec)
    return dot_product.tolist()
  else:
    return -1


pass