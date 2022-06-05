import pandas as pd

# function to load the dataset
def load_dataset(
    url=None,
    filename=None,
    file_type="csv",
    source="gdrive",
    cols=None,
    low_memory=False,
):
    if source == "gdrive":
        path = "https://drive.google.com/uc?export=download&id=" + url.split("/")[-2]
    elif source == "kaggle":
        path = f"/content/{filename}.{file_type}"
    if file_type == "csv":
        df = pd.read_csv(path, usecols=cols, low_memory=low_memory)
    elif file_type == "xlsx":
        df = pd.read_excel(path, usecols=cols, low_memory=low_memory)

    # address duplicates
    df = remove_dups(df)
    # # address missing values
    # impute_missing(df)
    # display the first 5 rows of the dataframe
    print(df.head())
    # print the df shape
    print(f"\nThe dataframe shape is {df.shape}\n")
    # display the df info
    print(df.info(show_counts=True))
    return df


def _load_local_dataset(path, file_type="csv", cols=None):
    if file_type == "csv":
        df = pd.read_csv(path, usecols=cols)
    else:
        df = pd.read_excel(path, usecols=cols)

    # remove duplicates
    df = remove_dups(df)
    return df


def remove_dups(df):
    # removing duplicates if any
    dup_rows = df.duplicated().sum()
    print(f"this dataset shape of {df.shape} has {dup_rows} duplicated rows")
    if dup_rows > 0:
        print(f"removing {dup_rows} duplicated rows")
        df = df.drop_duplicates()
    else:
        print("nothing to do, returning the original dataframe")

    return df
