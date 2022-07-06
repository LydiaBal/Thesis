import numpy as np
import pandas as pd
from numpy.linalg import norm

def cosineSim(user,df):
    apart_cosines = []
    for apartment in df:
        cosine = np.dot(user,apartment[1:])/(norm(user)*norm(apartment[1:]))
        apart_cosines.append((apartment[0],cosine))
    apart_cosines.sort(key = lambda x: x[1],reverse=True)
    return apart_cosines

def ExtractInfo(df):
    df = df.drop('neighbourhood_cleansed', axis=1)
    df = df.drop('accommodates', axis=1)
    df = df.drop('bathrooms', axis=1)
    df = df.drop('bedrooms', axis=1)
    df = df.drop('beds', axis=1)
    df = df.drop('daily_price', axis=1)
    df = df.drop('number_of_reviews', axis=1)
    df = df.drop('review_scores_rating', axis=1)
    df = df.drop('review_scores_location', axis=1)
    df = df.drop('Wheelchair_accessible', axis=1)
    df = df.drop('Pets_allowed', axis=1)


    return df

def Recommended(dfapartments, user,people,maxprice, minlocscore, minrevscore, wheelchair):
    # Get attributes for cosine sim
   attributesdf = ExtractInfo(dfapartments)
   attributeslist = df_to_array(attributesdf)

   #  Sort apartments according to user preferences
   sortedapart = cosineSim(user, attributeslist)
   sorted_apartments_id = [a_tuple[0] for a_tuple in sortedapart]

   dfapartments = dfapartments.set_index('id')
   dfapartments = dfapartments.reindex(sorted_apartments_id)

   #Return only those on which filters apply
   dfapartments = dfapartments[dfapartments['accommodates'] == people ]

   dfapartments = dfapartments[dfapartments['daily_price'] <= (maxprice + 10) ]
   dfapartments = dfapartments[dfapartments['daily_price'] >= (maxprice - 10) ]

   dfapartments = dfapartments[dfapartments['review_scores_location'] <= (minlocscore + 1) ]
   dfapartments = dfapartments[dfapartments['review_scores_location'] >= (minlocscore - 1) ]

   dfapartments = dfapartments[dfapartments['review_scores_rating'] >= (minrevscore - 10) ]
   dfapartments = dfapartments[dfapartments['review_scores_rating'] <= (minrevscore + 10)]


   if(wheelchair == 'on'):
      dfapartments = dfapartments[dfapartments['Wheelchair_accessible'] == 1 ]

   #Choose 5 best and get rid of unessecary columns
   return df_to_array(dfapartments[0:5])

#function to transform a dataframe into a list of lists
def df_to_array(df):
    data = []
    headers = list(df)
    for idx, i in enumerate(df.iterrows()):

        datarow = []
        for idy, h in enumerate(headers):
            datarow.append(df.iloc[idx,idy])

        data.append(datarow)

    return data
