from flask import Flask, request, render_template
import pickle
import numpy as np
filename = 'pizza_price_final.sav'
app = Flask(__name__)
def get_pred_price(loaded_model,inch,restau,cheese,musroom,spicy):
    hotel={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20}
    param=[inch,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,cheese,musroom,spicy]
    if restau in hotel.keys():
        param[hotel[restau]]=1
    price=loaded_model.predict([np.array(param)])
    return price

loaded_model = pickle.load(open(filename, 'rb'))

def convert_to_cad(price):
    price = price*0.015
    return price


predict = 0
restuarant = 'None'
yesno = {'yes':1,'no':0}
@app.route('/', methods=['POST','GET'])
def my_form_post():
    global predict
    global restuarant
    error = ""
    if request.method == 'GET':
        # Form being submitted; grab data from form.
        if request.args:
            size = request.args.get('Size')
            restuarant = request.args.get('Restuarant')
            extr_cheese = yesno[request.args.get('extr_cheese')]
            extr_mushroom = yesno[request.args.get('extr_mushroom')]
            extr_spicy = yesno[request.args.get('extr_spicy')]
        
        #print(size,restuarant,extr_cheese,extr_mushroom,extr_spicy
            price = get_pred_price(loaded_model,size,restuarant,extr_cheese,extr_mushroom,extr_spicy)
            predict = price[0]
            #predict = convert_to_cad(price)
        print(predict)
    # Render the sign-up page
    return render_template('index.html', prediction_text='Price of the Pizza from Restaurant {} is $ {}'.format(restuarant,predict))

if __name__ == "__main__":
    app.run()