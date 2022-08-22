import pandas as pd
import Preprocessing as prec
import SkylineAlg 

if __name__== "__main__":

    #read csv file and create dataframe
    dataset_name = "Airbnb_Milan.csv"
    dfapart = pd.read_csv(dataset_name, encoding="ISO-8859-1", na_values="")

    #preprocess dataframe
    processeddf = prec.ApartmentsPreprocess(dfapart)

    print ("Header i want in total = ", list(processeddf))
    headers = list(processeddf)
    print(len(list(processeddf)))

    
    #preprocess dataframe for skyline algorithm
    finalsky = []
    for i in range(1,13):
        processeddfsky = prec.SkylinePreprocess(processeddf,i)

    # transform dataframe to list of lists
        data = prec.df_to_array(processeddfsky)
    # print(data)

        # N = len(data[1])
        # print("Number of attributes:", N-1)
        print('len of data', len(data))
        sk = SkylineAlg.BNL(data, 3)
        # print(sk)
        if(len(sk)>0):
            for j in sk:
                # print(data[j])
                finalsky.append(data[j][0])
        print(len(sk))
    print(len(finalsky))

    resultsdf= processeddf[processeddf['id'].isin(finalsky)]
    resultsdf.to_csv("resultsdf.csv", index = False)

