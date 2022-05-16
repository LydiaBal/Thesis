from cgitb import html
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


user = [0,0,0,0,0,0,0,0,0,0,0]
@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     if request.form.get('action1') == 'TV':
    #         user[0] = 1
    #     if  request.form.get('action2') == 'WiFi':
    #         user[1] = 1
    #     if  request.form.get('action3') == 'Air Condition':
    #         user[2] = 1
    #     if  request.form.get('action4') == 'Kitchen':
    #         user[3] = 1
    #     if  request.form.get('action5') == 'Breakfast':
    #         user[4] = 1
    #     if  request.form.get('action6') == 'Elevator':
    #         user[5] = 1
    #     if  request.form.get('action7') == 'Heating':
    #         user[6] = 1
    #     if  request.form.get('action8') == 'Washer':
    #         user[7] = 1
    #     if  request.form.get('action9') == 'Iron':
    #         user[8] = 1
    #     if  request.form.get('action10') == 'Luggage dropoff':
    #         user[9] = 1
    #     if  request.form.get('action11') == 'Smoking allowed':
    #         user[10] = 1
    #     else:
    #         pass # unknown
    #     print(user)
    return render_template("index.html")

@app.route('/results', methods=['POST','GET'])
def results():
   print(request.args.get('action1'))
   print(request.form.get('action2'))
   print(request.form.get('action3'))
   print(request.form.get('action4'))
   print(request.form.get('action5'))
   print(request.form.get('action6'))
   print(request.form.get('action7'))
   print(request.form.get('action8'))
   print(request.form.get('action9'))
   print(request.form.get('action10'))
   print(request.form.get('action11'))


#    print(request)
#    if request.form.get("action1"):
#         print('clicked')
#    projectpath = request.files['action1']
#    print(projectpath)
   return 'Here are your results'

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=81)