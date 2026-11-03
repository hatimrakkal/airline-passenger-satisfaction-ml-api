import numpy as np, pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


NUM_VAR: list = [
    "Age", 
    "Flight Distance", 
    "Departure Delay in Minutes", 
    "Arrival Delay in Minutes"
]

CAT_VAR: list = [
    "Gender", 
    "Customer Type", 
    "Type of Travel", 
    "Class"
]

ORD_VAR: list = [
    "Inflight wifi service", "Departure/Arrival time convenient", "Ease of Online booking", 
    "Gate location", "Food and drink", "Online boarding", "Seat comfort", 
    "Inflight entertainment", "On-board service", "Leg room service", 
    "Baggage handling", "Checkin service", 
    "Inflight service", "Cleanliness"
]

def load_data(path: str) -> pd.DataFrame:
    """
    Load the airline data from the CSV file.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded airline data.
    """
    return pd.read_csv(path)

def add_log_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add log-transformed features for 'Departure Delay in Minutes' and 'Arrival Delay in Minutes'.

    Parameters:
    df (pd.DataFrame): The input DataFrame.

    Returns:
    pd.DataFrame: The DataFrame with added log-transformed features.
    """
    df = df.copy()
    df["Departure Delay lg"] = np.log1p(df["Departure Delay in Minutes"])
    df["Arrival Delay lg"] = np.log1p(df["Arrival Delay in Minutes"])

    return df

def fit_preprocessor(df: pd.DataFrame) -> dict:
    """
    Fit a preprocessor to the airline data by calculating bounds for continuous variables and determining the dummy column set for categorical variables.
    """

    df = add_log_features(df)

    # Learn the exact dummy column set from training data
    dummy_cols = pd.get_dummies(df, columns=CAT_VAR, drop_first=True).columns.tolist()

    return {"dummy_cols": dummy_cols}


def transform(df: pd.DataFrame, state: dict) -> pd.DataFrame:

    df = add_log_features(df)

    df = pd.get_dummies(df, columns=CAT_VAR, drop_first=True, dtype=float)
    # Align to training columns — this is the key line that prevents skew
    df = df.reindex(columns=state["dummy_cols"], fill_value=0)

    df = df.drop(columns=["id", "Arrival Delay lg"])

    return df


class Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X: pd.DataFrame, y=None):
        self.state_ = fit_preprocessor(X)
        self.feature_names_ = None
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        return transform(X, self.state_)