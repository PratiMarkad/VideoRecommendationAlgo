from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(y_true, y_pred):
    """Calculate MAE and RMSE for evaluation."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Root Mean Square Error (RMSE): {rmse}")
    return mae, rmse

if __name__ == "__main__":
    # Test evaluation metrics
    y_true = [4, 5, 3, 4]
    y_pred = [4.1, 4.8, 3.5, 3.9]
    evaluate_model(y_true, y_pred)
