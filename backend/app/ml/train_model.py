import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from backend.app.ml.preprocess import preprocess_data

def train_model(df, numeric_features, categorical_features, target_column, save_path="saved_models/xgb_model.pkl"):
    """
    Train an XGBoost classifier on the given dataset and save the trained model.
    """
    # Preprocess data
    X, preprocessor = preprocess_data(df, numeric_features, categorical_features)
    y = df[target_column]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.4f}, ROC-AUC: {roc_auc:.4f}")

    # Save model and preprocessor
    joblib.dump({"model": model, "preprocessor": preprocessor}, save_path)
    print(f"Trained model saved to {save_path}")

    return model, preprocessor