import numpy as np
def precision(y_true, y_pred):
	# Your code here
	true_positives = np.sum((y_pred == 1) & (y_true == 1))
	false_positives = np.sum((y_pred == 1) & (y_true == 0))
	predicted_positives = true_positives + false_positives
    if predicted_positives == 0:
        return 0.0
	return float(true_positives / predicted_positives)
