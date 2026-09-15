import numpy as np
def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
	h_t = np.array(initial_hidden_state)
    Wx = np.array(Wx)
    Wh = np.array(Wh)
    b = np.array(b)
	for x_t in input_sequence:
        x_t = np.array(x_t)
        h_t = np.tanh(np.dot(Wx, x_t) + np.dot(Wh, h_t) + b)
	return np.round(h_t,4).tolist()