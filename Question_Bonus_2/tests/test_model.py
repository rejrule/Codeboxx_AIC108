import os
import pickle
import pytest
import numpy as np

def test_model_file_exists():
    assert os.path.exists("model.pkl"), "model.pkl was not created."

def test_model_can_predict():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])  # typical Iris sample
    prediction = model.predict(sample)
    assert prediction.shape == (1,), "Model did not return a single prediction."

