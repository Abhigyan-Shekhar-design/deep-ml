import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    # Your code here
    sm=[]
    d=0
    for j in range(len(scores)):
        d+=np.exp(scores[j]-max(scores))
    for i in range(len(scores)):
        sm.append(np.exp(scores[i]-max(scores))/d)
    return sm