from sklearn.datasets import fetch_california_housing
from sklearn.utils import Bunch
import pandas as pd


def main():
    data: Bunch = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["MedHouseVal"] = data.target

    print("Shape:", df.shape)
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    main()