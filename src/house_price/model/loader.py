import joblib
from house_price.config import MODEL_PATH, FEATURES_PATH

_model = None
_features = None


def load_model():
    """Load model and features into memory. Call once at startup."""
    global _model, _features
    _model = joblib.load(MODEL_PATH)
    _features = joblib.load(FEATURES_PATH)


def get_model():
    """Return the loaded model, raising if not loaded yet."""
    if _model is None:
        raise RuntimeError("Model not loaded. Call load_model() at startup.")
    return _model


def get_features():
    """Return the loaded feature list, raising if not loaded yet."""
    if _features is None:
        raise RuntimeError("Features not loaded. Call load_model() at startup.")
    return _features