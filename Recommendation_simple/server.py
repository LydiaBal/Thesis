from cgitb import html
from itertools import count
from pickle import NONE
from typing import Counter
from flask import Flask, request
from flask import render_template, redirect, url_for
import mysqlx
from numpy import array
import RecFunctions as rec
import pandas as pd
import numpy as np

app = Flask(__name__)

user = [0,0,0,0,0,0,0,0,0,0,0]
@app.route('/', methods=['GET', 'POST'])
def index():
   for i in range(len(user)):
      user[i] = 0
   print('Initialization of user array', user)
   return render_template("demo.html")

@app.route('/pref', methods=['GET', 'POST'])
def pref():
   show_ap = []
   table = 0
   for i in range(len(user)):
      user[i] = 0
   print('Initialization of user array', user)

   dataset_name = "processeddf.csv"
   dfapartments = pd.read_csv(dataset_name, encoding="ISO-8859-1", na_values="")

   if request.args.get('People') != None :
      table = 1
   #Return only those on which filters apply
      dfapartments = dfapartments[dfapartments['accommodates'] == int(request.args.get('People')) ]
      dfapartments = dfapartments[dfapartments['daily_price'] <= int(request.args.get('maxPrice')) ]
      dfapartments = dfapartments[dfapartments['review_scores_location'] >= int(request.args.get('locationminscores')) ]
      dfapartments = dfapartments[dfapartments['review_scores_rating'] >= int(request.args.get('reviewsminscores')) ]
      if(request.args.get('wheelchair') == 'on'):
         print('got in here')
         dfapartments = dfapartments[dfapartments['Wheelchair_accessible'] == 1 ]
      show_ap = rec.df_to_array(dfapartments)

   return render_template("index.html",wheelchair = request.args.get('wheelchair'),  show_table = table, my_list = show_ap)


@app.route('/results', methods=['POST','GET'])
def results():

   # Get user preferences
   if request.args.get('TV') == 1:
      user[0] = 1
   if request.args.get('WiFi') != None:
      user[1] = 1
   if request.args.get('air_condition') != None:
      user[2] = 1
   if request.args.get('kitchen') != None:
      user[3] = 1
   if request.args.get('breakfast') != None:
      user[4] = 1
   if request.args.get('elevator') != None:
      user[5] = 1
   if request.args.get('heating') != None:
      user[6] = 1
   if request.args.get('washer') != None:
      user[7] = 1
   if request.args.get('iron') != None:
      user[8] = 1
   if request.args.get('luggage') != None:
      user[9] = 1
   if request.args.get('smoking') != None:
      user[10] = 1
   print('User list is:', user)

   # Get apartments from skyline
   dataset_name = "processeddf.csv"
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
   dfapartments = dfapartments[dfapartments['accommodates'] == int(request.args.get('people')) ]
   print(dfapartments)
   dfapartments = dfapartments[dfapartments['daily_price'] <= int(request.args.get('maxPrice')) + 10 ]
   dfapartments = dfapartments[dfapartments['daily_price'] >= int(request.args.get('maxPrice')) - 10 ]
   print(dfapartments)
   dfapartments = dfapartments[dfapartments['review_scores_location'] <= (int(request.args.get('locationminscores')) + 1) ]
   dfapartments = dfapartments[dfapartments['review_scores_location'] >= (int(request.args.get('locationminscores')) - 1) ]
   print(dfapartments)
   dfapartments = dfapartments[dfapartments['review_scores_rating'] >= (int(request.args.get('reviewsminscores')) - 10) ]
   dfapartments = dfapartments[dfapartments['review_scores_rating'] <= (int(request.args.get('reviewsminscores')) + 10)]
   print(dfapartments)

   if(request.args.get('wheelchair') == 'on'):
      dfapartments = dfapartments[dfapartments['Wheelchair_accessible'] == 1 ]


   #Choose 5 best and get rid of unessecary columns
   show_ap = rec.df_to_array(dfapartments[0:5])
   print(show_ap)
   # dfapartments.to_csv("sortedapartments.csv", index = False)
   return render_template('results.html', my_list = show_ap)

@app.route('/questionnaire', methods=['POST','GET'])
def questionnaire():
   return render_template('questionnaire.html')

@app.route('/adios', methods=['POST','GET'])
def adios():
   acurate = 1
   user_voting = []
   if request.args.get('question0') != None and request.args.get('question1') != None and request.args.get('question2') != None and request.args.get('question3') != None and request.args.get('question4') != None and request.args.get('question5') != None and request.args.get('question6') != None and request.args.get('question7') != None and request.args.get('question8') != None :
      user_voting.append(int(request.args.get('age')))
      user_voting.append(int(request.args.get('question0')))
      user_voting.append(int(request.args.get('question1')))
      user_voting.append(int(request.args.get('question2')))
      user_voting.append(int(request.args.get('question3')))
      user_voting.append(int(request.args.get('question4')))
      user_voting.append(int(request.args.get('question5')))
      user_voting.append(int(request.args.get('question6')))
      user_voting.append(int(request.args.get('question7')))
      user_voting.append(int(request.args.get('question8')))
      print(user_voting)
      try:
         dataset_name = "voted.csv"
         votes = pd.read_csv(dataset_name, encoding="ISO-8859-1", na_values="")
      except:
         votes = pd.DataFrame(columns=['age','familiarity','mentally_demanding','pace_of_task','satisfaction_choice','satisfaction_rec','searching_effort','discouraged','challenging','not_appealing'])
      votes.loc[-1] = user_voting
      votes.index = votes.index + 1
      new_votes = votes.sort_index()
      new_votes.to_csv("voted.csv", index = False)
         
         
   else:
      acurate = 0
      
   return render_template('adios.html', valid = acurate)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=81)