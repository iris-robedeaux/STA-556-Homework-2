#import libraries
import pandas as pd

#define the cleaner function
def cleanDataType(df):
    #make release date an actual date type
    df["Release date (datetime)"] = pd.to_datetime(
        df["Release date (datetime)"],
        format="%B %d, %Y"
    )

    #remove the % from the RT score
    df["rotten_tomatoes"] = pd.to_numeric(
        df["rotten_tomatoes"].astype(str).str.replace("%", "", regex=False)
    ).astype("Int64")

    #convert score to integers
    df["imdb"] = (pd.to_numeric(df["imdb"], errors="coerce") * 10).round().astype("Int64")
    df["metascore"] = pd.to_numeric(df["metascore"], errors="coerce").astype("Int64")
    df["rotten_tomatoes"] = pd.to_numeric(df["rotten_tomatoes"], errors="coerce").astype("Int64")

    #if there's more than one langauge, select just the first
    df["Language"] = df["Language"].apply(
        lambda x: (x[0] if x else None) if isinstance(x, list) else x
    )

    #return the cleaned df
    return df

#get percentages for the representation of each language
def summCat(df, column):
    props = df[column].value_counts(normalize=True)

    props.tolist()            # just the proportions
    props.index.tolist()      # the matching language names
    return (props * 100).round(1)    # as percentages

def summQuant( df, columns ):
    return df[columns].agg(["mean", "median", "min", "max"])