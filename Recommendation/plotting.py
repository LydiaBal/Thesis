import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('voted_skyline.csv')

# PREFERENCE CORRELATION WITH EXPERIENCE
ones_fam=[]
twos_fam=[]

for (i,item) in enumerate(df['which_rec']):
    if item == 1:
        ones_fam.append(df['discouraged'][i])
    else:
        twos_fam.append(df['discouraged'][i])

exp_1 = sum(ones_fam)/len(ones_fam)
exp_2 = sum(twos_fam)/len(twos_fam)

plt.bar(['Skyline Recommender', 'Simple Recommender'], [exp_1,exp_2], color ='c', width = 0.3)
plt.title('How discouraged were you')
plt.show()


# #PREFERENCE
# ones = 0
# twos = 0
# preference = list(df['which_rec'])
# for i in preference:
#     if i == 1:
#         ones = ones + 1
#     else:
#         twos = twos + 1

# data = {'Skyline Recommender':ones, 'Simple Recommender':twos}
# titles = list(data.keys())
# values = list(data.values())
 
# plt.bar(titles, values, color ='c', width = 0.3)
# plt.show()


# #NEGATIVE VALUES AS WELL | PREFERENCE SATISFACTION
# satisfaction_rec1 = df['satisfaction_rec1'].sum()/(len(df.index)-1)
# satisfaction_rec2 = df['satisfaction_rec2'].sum()/(len(df.index)-1)
# not_appealing1 = df['not_appealing1'].sum()/(len(df.index)-1)
# not_appealing2 = df['not_appealing2'].sum()/(len(df.index)-1)

# rec_1 = [satisfaction_rec1, not_appealing1]
# rec_1_dev =[1,2]
# rec_2 = [satisfaction_rec2, not_appealing2]
# rec_2_dev = [1.2, 1.4]

# X = ['Satisfaction','Not Appealing results']

# X_axis = np.arange(len(X))


# plt.bar(X_axis - 0.15, rec_1, 0.3, label = 'Skyline Recommender',color='y', yerr=rec_1_dev)
# plt.bar(X_axis + 0.15, rec_2, 0.3, label = 'Simple Recommender',color='c',yerr=rec_2_dev)

# plt.xticks(X_axis, X)
# plt.legend()
# plt.show()

# #ONLY POSITIVE VALUES | PREFERENCE SATISFACTION
# rec_1 = [6.42, 2.84]
# rec_1_dev =[0.8,1.9]
# rec_2 = [5.42, 3.9]
# rec_2_dev = [1.2, 1.4]

# X = ['Satisfaction','Not Appealing results']

# X_axis = np.arange(len(X))


# plt.bar(X_axis - 0.15, rec_1, 0.3, label = 'Skyline Recommender',color='y', yerr=rec_1_dev)
# plt.bar(X_axis + 0.15, rec_2, 0.3, label = 'Simple Recommender',color='c',yerr=rec_2_dev)

# plt.xticks(X_axis, X)
# plt.legend()
# plt.show()

