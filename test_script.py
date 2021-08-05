import pickle
import numpy as np
filename = 'pizza_price_final.sav'

def get_pred_price(loaded_model,inch,restau,cheese,musroom,spicy):
    hotel={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20}
    param=[inch,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,cheese,musroom,spicy]
    if restau in hotel.keys():
        param[hotel[restau]]=1
    price=loaded_model.predict([np.array(param)])
    return price

loaded_model = pickle.load(open(filename, 'rb'))

price = get_pred_price(loaded_model,12,'A',1,1,0)
print('Price of pizza is: ',price[0])