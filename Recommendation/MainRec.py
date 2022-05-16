import pandas as pd
import RecFunctions as rec


if __name__== "__main__":
    # Get apartments from skyline
    dataset_name = "resultsdf.csv"
    dfapartments = pd.read_csv(dataset_name, encoding="ISO-8859-1", na_values="")

    # Get attributes for cosine sim
    attributesdf = rec.ExtractInfo(dfapartments)
    attributeslist = rec.df_to_array(attributesdf)

    # User preferences
    user = [0,1,0,0,0,1,1,1,1,0,1,0,1]

    # Sort apartments according to user preferences
    sortedapart = rec.cosineSim(user, attributeslist)
    print(sortedapart)

    