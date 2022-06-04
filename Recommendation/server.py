from cgitb import html
from itertools import count
from pickle import NONE
from typing import Counter
from flask import Flask, request
from flask import render_template, redirect, url_for
from numpy import array
import RecFunctions as rec
import pandas as pd

app = Flask(__name__)

page = 0

user = [0,0,0,0,0,0,0,0,0,0,0]
@app.route('/', methods=['GET', 'POST'])
def index():
   global page
   page = 0
   for i in range(len(user)):
      user[i] = 0
   print('Initialization of user array', user)
   return render_template("demo.html")

@app.route('/pref', methods=['GET', 'POST'])
def pref():
   global page
   page = 0
   for i in range(len(user)):
      user[i] = 0
   print('Initialization of user array', user)
   return render_template("index.html")

@app.route('/results', methods=['POST','GET'])
def results():

   # Get user preferences
   if request.args.get('action1') != None:
      user[0] = 1
   if request.args.get('action2') != None:
      user[1] = 1
   if request.args.get('action3') != None:
      user[2] = 1
   if request.args.get('action4') != None:
      user[3] = 1
   if request.args.get('action5') != None:
      user[4] = 1
   if request.args.get('action6') != None:
      user[5] = 1
   if request.args.get('action7') != None:
      user[6] = 1
   if request.args.get('action8') != None:
      user[7] = 1
   if request.args.get('action9') != None:
      user[8] = 1
   if request.args.get('action10') != None:
      user[9] = 1
   if request.args.get('action11') != None:
      user[10] = 1
   print('User list is:', user)

   # Get apartments from skyline
   dataset_name = "resultsdf.csv"
   dfapartments = pd.read_csv(dataset_name, encoding="ISO-8859-1", na_values="")

   # Get attributes for cosine sim
   attributesdf = rec.ExtractInfo(dfapartments)
   attributeslist = rec.df_to_array(attributesdf)

   #  Sort apartments according to user preferences
   sortedapart = rec.cosineSim(user, attributeslist)
   sorted_apartments_id = [a_tuple[0] for a_tuple in sortedapart]
   print(len(sorted_apartments_id))

   dfapartments = dfapartments.set_index('id')
   dfapartments = dfapartments.reindex(sorted_apartments_id)
   print('Apartments order', sortedapart)

   #Return only those on which filters apply
   dfapartments = dfapartments[dfapartments['accommodates'] == int(request.args.get('People')) ]
   print(dfapartments)
   dfapartments = dfapartments[dfapartments['daily_price'] <= int(request.args.get('maxPrice')) ]
   # dfapartments = dfapartments[dfapartments['daily_price'] >= int(request.args.get('minPrice')) ]
   # dfapartments = dfapartments[dfapartments['review_scores_location'] <= int(request.args.get('locationmaxscores')) ]
   dfapartments = dfapartments[dfapartments['review_scores_location'] >= int(request.args.get('locationminscores')) ]
   # dfapartments = dfapartments[dfapartments['review_scores_rating'] <= int(request.args.get('reviewsmaxscores')) ]
   dfapartments = dfapartments[dfapartments['review_scores_rating'] >= int(request.args.get('reviewsminscores')) ]
   if(request.args.get('wheelchair') == 'on'):
      dfapartments = dfapartments[dfapartments['Wheelchair_accessible'] == 1 ]


   #Choose 5 best and get rid of unessecary columns
   show_ap = rec.df_to_array(dfapartments[0:5])
   print(show_ap)
   # dfapartments.to_csv("sortedapartments.csv", index = False)

   return render_template('results.html', my_list = show_ap)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=81)