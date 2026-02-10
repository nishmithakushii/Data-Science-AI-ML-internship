import numpy as np
scores=np.random.randint(50,101,size=(5,3))
mean_scores=scores.mean(axis=0)
centered_scores=scores-mean_scores
print("Original scores:\n",scores)
print("\nMean scores:\n",mean_scores)
print("\nCentered scores:\n",centered_scores)