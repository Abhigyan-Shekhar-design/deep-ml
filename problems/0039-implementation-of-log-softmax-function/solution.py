import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	ls=[]
	for i in range(len(scores)):
		ls.append(scores[i]-np.log(np.sum(np.exp(scores))))
	return ls