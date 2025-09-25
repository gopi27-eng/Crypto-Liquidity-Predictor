import joblib
import os
import warnings

# Suppress joblib warnings during model loading
warnings.filterwarnings("ignore", category=UserWarning, module="joblib")

def load_artifacts():
    """
    Loads the pre-trained model and target encoder from disk.

    Returns:
        tuple: A tuple containing the loaded model and encoder.
               (best_model, encoder)
    Raises:
        FileNotFoundError: If the model or encoder files are not found.
    """
    # Define the file paths for the saved artifacts
    # The fix is to explicitly include the 'models' directory in the path.
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'Randomforest_Regression_model.pkl')
    encoder_path = os.path.join(current_dir, 'TargetEncoder.pkl')

    print("Attempting to load model and encoder...")

    # Load the trained model
    try:
        best_model = joblib.load(model_path)
        print("Model loaded successfully.")
    except FileNotFoundError:
        # Since you are running from the parent directory, let's adjust the path.
        model_path = os.path.join(current_dir, 'models', 'Randomforest_Regression_model.pkl')
        encoder_path = os.path.join(current_dir, 'models', 'TargetEncoder.pkl')
        try:
            best_model = joblib.load(model_path)
            print("Model loaded successfully (from subdirectory).")
        except FileNotFoundError:
            raise FileNotFoundError(f"Model file not found at: {model_path}")

    # Load the fitted target encoder
    try:
        encoder = joblib.load(encoder_path)
        print("Encoder loaded successfully.")
    except FileNotFoundError:
        # Since you are running from the parent directory, let's adjust the path.
        encoder_path = os.path.join(current_dir, 'models', 'TargetEncoder.pkl')
        try:
            encoder = joblib.load(encoder_path)
            print("Encoder loaded successfully (from subdirectory).")
        except FileNotFoundError:
            raise FileNotFoundError(f"Encoder file not found at: {encoder_path}")

    return best_model, encoder

if __name__ == '__main__':
    # This block allows you to test the artifact loading
    try:
        model, encoder = load_artifacts()
        print("\nArtifacts loaded successfully for testing.")
        print("Model type:", type(model).__name__)
        print("Encoder type:", type(encoder).__name__)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure 'Randomforest_Regression_model.pkl' and 'TargetEncoder.pkl' are in the correct directory.")
