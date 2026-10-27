import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	

	 mean_matrix = np.array(matrix)

	 if mode == "row":
		means = np.mean(mean_matrix , axis = 1)
	 else:
		means = np.mean(mean_matrix , axis = 0)
	 
	 return means.tolist() 

  