from cgitb import html
from pickle import NONE
from flask import Flask, request
from flask import render_template
from numpy import array
import RecFunctions as rec
import pandas as pd

app = Flask(__name__)


user = [0,0,0,0,0,0,0,0,0,0,0]
@app.route('/', methods=['GET', 'POST'])
def index():
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

   dfapartments = dfapartments.set_index('id')
   dfapartments = dfapartments.reindex(sorted_apartments_id)
   # print(dfapartments)
   print('Apartments order', sortedapart)
   dfapartments.to_csv("sortedapartments.csv", index = False)

   return render_template('results.html',  tables=[dfapartments.to_html(classes='data',index = False)], titles=dfapartments.columns.values)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=81)