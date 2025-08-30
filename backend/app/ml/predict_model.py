import joblib
import pandas as pd

def predict(model_path, input_df):
    """
    Load a saved model and preprocessor, and predict outcomes for input data.
    """
    saved_objects = joblib.load(model_path)
    model = saved_objects["model"]
    preprocessor = saved_objects["preprocessor"]

    # Preprocess input
    X = preprocessor.transform(input_df)

    # Make predictions
    predictions = model.predict(X)
    prediction_probs = model.predict_proba(X)[:, 1]  # probability for positive class

    return predictions, prediction_probs