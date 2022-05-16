import pandas as pd
import numpy as np

def ApartmentsPreprocess(df):

    #drop unwanted columns
    df = df.drop('host_is_superhost', axis=1)
    df = df.drop('Unnamed: 0', axis=1)
    df = df.drop('host_id', axis=1)
    df = df.drop('host_location', axis=1)
    df = df.drop('host_response_time', axis=1)
    df = df.drop('host_response_rate', axis=1)
    df = df.drop('host_total_listings_count', axis=1)
    df = df.drop('host_has_profile_pic', axis=1)
    df = df.drop('host_identity_verified', axis=1)
    df = df.drop('zipcode', axis=1)
    df = df.drop('latitude', axis=1)
    df = df.drop('longitude', axis=1)
    df = df.drop('room_type', axis=1)
    df = df.drop('bed_type', axis=1)
    df = df.drop('security_deposit', axis=1)
    df = df.drop('cleaning_fee', axis=1)
    df = df.drop('guests_included', axis=1)
    df = df.drop('extra_people', axis=1)
    df = df.drop('minimum_nights', axis=1)
    df = df.drop('availability_30', axis=1)
    df = df.drop('availability_60', axis=1)
    df = df.drop('availability_90', axis=1)
    df = df.drop('availability_365', axis=1)
    df = df.drop('instant_bookable', axis=1)
    df = df.drop('cancellation_policy', axis=1)
    df = df.drop('require_guest_profile_picture', axis=1)
    df = df.drop('require_guest_phone_verification', axis=1)
    df = df.drop('Host_greets_you', axis=1)
    df = df.drop('Paid_parking_on_premises', axis=1)
    df = df.drop('Long_term_stays_allowed', axis=1)
    df = df.drop('Doorman', axis=1)
    df = df.drop('Suitable_for_events', axis=1)
    df = df.drop('24_hour_check_in', axis=1)
    df = df.drop('review_scores_accuracy', axis=1)
    df = df.drop('review_scores_cleanliness', axis=1)
    df = df.drop('review_scores_checkin', axis=1)
    df = df.drop('review_scores_communication', axis=1)
    df = df.drop('review_scores_value', axis=1)



    dfsampled = df.copy(deep=True)
    dfsampled.to_csv("processeddf.csv", index = False)
    return df

# Keep only the attributes needed for BNL
def SkylinePreprocess(df,people):
    df = df.drop('neighbourhood_cleansed', axis=1)
    df = df.drop('bathrooms', axis=1)
    df = df.drop('bedrooms', axis=1)
    df = df.drop('beds', axis=1)
    df = df.drop('TV', axis=1)
    df = df.drop('WiFi', axis=1)
    df = df.drop('Air_Condition', axis=1)
    df = df.drop('Wheelchair_accessible', axis=1)
    df = df.drop('Kitchen', axis=1)
    df = df.drop('Breakfast', axis=1)
    df = df.drop('Elevator', axis=1)
    df = df.drop('Heating', axis=1)
    df = df.drop('Washer', axis=1)
    df = df.drop('Iron', axis=1)
    df = df.drop('Luggage_dropoff_allowed', axis=1)
    df = df.drop('Pets_allowed', axis=1)
    df = df.drop('Smoking_allowed', axis=1)
    df = df.drop('number_of_reviews', axis=1)

    df = df[df.accommodates == people ]
    df = df.drop('accommodates', axis=1)

    price_range = [1, 2, 3, 4, 5, 6, 7]
    cut_bins_price = [0, 100, 200, 300, 400, 700, 1000, 10000]
    df['price_sky'] = pd.cut(df['daily_price'], bins=cut_bins_price, labels=price_range)
    df = df.drop('daily_price', axis=1)

    score_range = [1, 2, 3, 4, 5]
    cut_bins_score = [0, 30, 50, 70, 80, 100]
    df['score_reviews_sky'] = pd.cut(df['review_scores_rating'], bins=cut_bins_score, labels=score_range)
    df = df.drop('review_scores_rating', axis=1)

    location_range = [1, 2, 3, 4, 5, 6]
    cut_bins_location = [0, 3, 5, 7, 8, 9, 10]
    df['location_sky'] = pd.cut(df['review_scores_location'], bins=cut_bins_location, labels=location_range)
    df = df.drop('review_scores_location', axis=1)

    dfcopy = df.copy(deep=True)
    dfcopy.to_csv('processeddfsky'+ str(people) +'.csv', index = False)
    return df


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