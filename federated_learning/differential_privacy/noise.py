# federated_learning/differential_privacy/noise.py
from diffprivlib.mechanisms import Gaussian

def add_noise(data, epsilon=0.5):
    mechanism = Gaussian(epsilon=epsilon, sensitivity=1.0)
    return mechanism.randomise(data)